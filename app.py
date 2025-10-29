from flask import Flask, render_template, request, jsonify, send_file, session, redirect, url_for
from flask_cors import CORS
from dotenv import load_dotenv
from datetime import datetime, timedelta
import openai
import httpx
import os
import io
from fpdf import FPDF
import firebase_admin
from firebase_admin import credentials, firestore
import json
from mpesa_integration import MpesaIntegration, SubscriptionManager

# Load .env variables
load_dotenv()

# Load API Keys
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Firebase Configuration for frontend
FIREBASE_CONFIG = {
    'apiKey': os.getenv('FIREBASE_API_KEY', 'AIzaSyDTm-ckLXcOcRM_4g5hTs94Tm4W_BUx-eI'),
    'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN', 'cbch-6178c.firebaseapp.com'),
    'projectId': os.getenv('FIREBASE_PROJECT_ID', 'cbch-6178c'),
    'appId': os.getenv('FIREBASE_APP_ID', '1:577618974847:web:730ae29830d14fc0a6c74a')
}

# OpenAI Client
openai_client = openai.OpenAI(api_key=OPENAI_KEY)

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_config.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Initialize M-Pesa and Subscription Manager
mpesa = MpesaIntegration()
subscription_manager = SubscriptionManager(db)

# Admin credentials (in production, use proper authentication)
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@careermentor.com')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')

# Authentication decorator
def admin_required(f):
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

# Load CBC summary
with open("static/CBC_SUMMARY.txt", "r", encoding="utf-8") as f:
    CBC_SUMMARY = f.read()

# ========= 🔁 Universal AI Helper =========
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")  # Default if not set

def ask_ai(messages, model="gpt-3.5-turbo", max_tokens=800, temperature=0.7):
    try:
        # ✅ Try Groq first
        if GROQ_API_KEY:
            response = httpx.post(
                url="https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": GROQ_MODEL,
                    "messages": messages,
                    "max_tokens": max_tokens,
                    "temperature": temperature
                },
                timeout=30
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]

        # 🔁 Fallback to OpenAI
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message.content

    except httpx.HTTPStatusError as http_err:
        print(f"🛑 Groq API error {http_err.response.status_code}: {http_err.response.text}")
    except Exception as e:
        print("AI Call Failed:", e)

    return None  # Return fallback for all failures

# ========== Routes ==========

@app.route('/')
def home():
    return render_template("index.html", cbc_explainer=CBC_SUMMARY[:600], firebase_config=FIREBASE_CONFIG)


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    email = data.get("email", "anonymous")

    system_prompt = (
        "You are an AI education mentor for Kenyan students under the Competency-Based Curriculum (CBC). "
        "Use the following reference when answering user questions. You can also use general education and career knowledge if needed.\n\n"
        f"{CBC_SUMMARY}\n\n"
        "Respond in clear, helpful, and localized language."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    reply = ask_ai(messages)

    if reply:
        # Save to Firebase
        try:
            db.collection("messages").add({
                "user": email,
                "email": email,
                "user_message": user_message,
                "ai_reply": reply,
                "timestamp": datetime.now()
            })
        except Exception as e:
            print(f"Error saving to Firebase: {e}")
        
        # Also save to local log file
        with open("logs.txt", "a", encoding="utf-8") as log:
            log.write(f"[{datetime.now()}] {email} > {user_message}\nAI: {reply}\n\n")
        
        return jsonify({"reply": reply})
    else:
        return jsonify({"reply": "Sorry, I had trouble answering. Please try again later."})


@app.route('/preview_cv_index', methods=['POST'])
def preview_cv_index():
    data = request.get_json()
    name = data.get("name", "")
    email = data.get("email", "")
    education = data.get("education", "")
    skills = data.get("skills", "")
    interests = data.get("interests", "")

    prompt = f"""
You are a professional CV writing assistant.
Using the following structured data, generate a detailed, professional CV in paragraph form, organized into sections like: Profile Summary, Education, Skills, and Career Interests.

Name: {name}
Email: {email}
Education Background: {education}
Key Skills: {skills}
Career Interests: {interests}

Write in a polished and formal tone suitable for job applications.
"""

    messages = [
        {"role": "system", "content": "You are a helpful assistant that writes professional CVs."},
        {"role": "user", "content": prompt}
    ]

    reply = ask_ai(messages)

    if not reply:
        return jsonify({"error": "CV generation failed"}), 500

    return jsonify({"preview": reply})



@app.route('/generate_cv', methods=['POST'])
def generate_cv():
    data = request.get_json()
    name = data.get("name", "Student")
    email = data.get("email", "unknown")
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # Create prompt to send to AI
    messages = [
        {"role": "system", "content": "You are a CV writing expert. Create a clean, modern CV using the user's details."},
        {"role": "user", "content": f"Name: {name}\nEmail: {email}\nDetails: {prompt}"}
    ]

    reply = ask_ai(messages)
    if not reply:
        return jsonify({"error": "CV generation failed"}), 500

    # Save CV download to Firebase
    try:
        db.collection("cv_downloads").add({
            "name": name,
            "email": email,
            "timestamp": datetime.now()
        })
    except Exception as e:
        print(f"Error saving CV download to Firebase: {e}")

    # ✅ Format the CV nicely into a PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    lines = reply.strip().split("\n")
    pdf.set_font("Arial", size=12)

    for line in lines:
        if ":" in line and line.strip().endswith(":"):
            # This is a section header
            pdf.set_font("Arial", style="B", size=12)
            pdf.multi_cell(0, 10, line.strip())
        elif ":" in line:
            # Key-value like Name: Jane Doe
            key, value = line.split(":", 1)
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(40, 10, f"{key.strip()}: ")
            pdf.set_font("Arial", style="", size=12)
            pdf.multi_cell(0, 10, value.strip())
        elif line.strip().startswith("-"):
            # Bullet point
            pdf.set_font("Arial", style="", size=12)
            pdf.multi_cell(0, 10, u"\u2022 " + line.strip().lstrip("-").strip())
        else:
            # Regular paragraph
            pdf.set_font("Arial", style="", size=12)
            pdf.multi_cell(0, 10, line.strip())

    # Output to BytesIO
    pdf_output = io.BytesIO()
    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    pdf_output.write(pdf_bytes)
    pdf_output.seek(0)

    return send_file(pdf_output, download_name="Generated_CV.pdf", as_attachment=True)



@app.route('/generate_pathway', methods=['POST'])
def generate_pathway():
    data = request.get_json()
    prompt = data.get("prompt", "")
    name = data.get("name", "Student")
    email = data.get("email", "unknown")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    system_prompt = """
You are an educational and career guidance expert helping Kenyan students understand the best CBC Senior School Pathway based on their unique strengths.

Your task is to:
1. Interpret the student's description using **Howard Gardner's Multiple Intelligences**.
2. Suggest the most suitable **CBC Senior School Pathway**.
3. Recommend possible **career options** aligned with the pathway.
4. Present it in a friendly, motivating tone.

Keep the output structured in these sections:
- Student Name
- Summary of Interests
- Matched Intelligences
- Suggested CBC Pathway
- Career Suggestions
- Motivational Message
"""

    user_prompt = f"""
Student Name: {name}
Email: {email}
Student's description: "{prompt}"
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    reply = ask_ai(messages)
    if not reply:
        return jsonify({"error": "Pathway generation failed"}), 500

    # Return preview in JSON first
    return jsonify({"preview": reply})

@app.route('/download_pathway_pdf', methods=['POST'])
def download_pathway_pdf():
    data = request.get_json()
    prompt = data.get("prompt", "")
    name = data.get("name", "Student")
    email = data.get("email", "unknown")

    # Reuse same system prompt as before
    system_prompt = """
You are an educational and career guidance expert helping Kenyan students understand the best CBC Senior School Pathway based on their unique strengths.

Your task is to:
1. Interpret the student's description using **Howard Gardner's Multiple Intelligences**.
2. Suggest the most suitable **CBC Senior School Pathway**.
3. Recommend possible **career options** aligned with the pathway.
4. Present it in a friendly, motivating tone.

Use these section headings:
- Student Name
- Summary of Interests
- Matched Intelligences
- Suggested CBC Pathway
- Career Suggestions
- Motivational Message
"""

    user_prompt = f"""
Student Name: {name}
Email: {email}
Student's description: "{prompt}"
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    reply = ask_ai(messages)
    if not reply:
        return jsonify({"error": "AI failed"}), 500

    # Save pathway download to Firebase
    try:
        db.collection("pathway_downloads").add({
            "name": name,
            "email": email,
            "prompt": prompt,
            "timestamp": datetime.now()
        })
    except Exception as e:
        print(f"Error saving pathway download to Firebase: {e}")

    # ✅ Format PDF with headers
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    lines = reply.split("\n")
    for line in lines:
        if line.strip().startswith("- ") or line.strip().endswith(":"):
            pdf.set_font("Arial", style="B", size=12)
        else:
            pdf.set_font("Arial", style="", size=12)
        safe_line = line.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, txt=safe_line)

    pdf_output = io.BytesIO()
    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    pdf_output.write(pdf_bytes)
    pdf_output.seek(0)

    return send_file(pdf_output, download_name="CBC_Pathway_Suggestion.pdf", as_attachment=True)



@app.route('/ai_assessment', methods=['POST'])
def ai_assessment():
    data = request.get_json()
    responses = data.get("responses", [])
    user_email = data.get("email", "anonymous")
    
    if not responses:
        return jsonify({"error": "Assessment responses required"}), 400
    
    # Create comprehensive assessment prompt
    assessment_prompt = f"""
    You are a professional career counselor conducting a comprehensive career assessment for a Kenyan student.
    
    Based on the following responses to career assessment questions, provide:
    1. Personality Type Analysis (using Big Five traits)
    2. Learning Style Assessment
    3. Career Interest Areas (Holland's RIASEC model)
    4. Strengths and Development Areas
    5. Recommended CBC Pathways
    6. Career Suggestions with salary expectations in Kenya
    7. Educational Roadmap
    8. Action Plan for next 2 years
    
    Student Responses: {responses}
    
    Format the response in clear sections with actionable insights.
    """
    
    messages = [
        {"role": "system", "content": "You are an expert career counselor specializing in Kenyan education and job market."},
        {"role": "user", "content": assessment_prompt}
    ]
    
    reply = ask_ai(messages, max_tokens=1500)
    
    if reply:
        # Save assessment to Firebase
        try:
            db.collection("assessments").add({
                "user": user_email,
                "email": user_email,
                "responses": responses,
                "assessment_result": reply,
                "timestamp": datetime.now()
            })
        except Exception as e:
            print(f"Error saving assessment: {e}")
        
        return jsonify({"assessment": reply})
    else:
        return jsonify({"error": "Assessment generation failed"}), 500

@app.route('/ai_interview_prep', methods=['POST'])
def ai_interview_prep():
    data = request.get_json()
    job_title = data.get("job_title", "")
    industry = data.get("industry", "")
    experience_level = data.get("experience_level", "entry")
    user_email = data.get("email", "anonymous")
    
    if not job_title:
        return jsonify({"error": "Job title required"}), 400
    
    interview_prompt = f"""
    You are an expert interview coach preparing a Kenyan job seeker for interviews.
    
    Job Title: {job_title}
    Industry: {industry}
    Experience Level: {experience_level}
    
    Provide:
    1. Common interview questions for this role in Kenya
    2. STAR method answers for behavioral questions
    3. Industry-specific technical questions
    4. Salary negotiation tips for Kenyan market
    5. Company research suggestions
    6. Follow-up email templates
    7. Interview day checklist
    
    Make it practical and Kenya-specific.
    """
    
    messages = [
        {"role": "system", "content": "You are an expert interview coach specializing in the Kenyan job market."},
        {"role": "user", "content": interview_prompt}
    ]
    
    reply = ask_ai(messages, max_tokens=1200)
    
    if reply:
        # Save interview prep to Firebase
        try:
            db.collection("interview_preps").add({
                "user": user_email,
                "email": user_email,
                "job_title": job_title,
                "industry": industry,
                "experience_level": experience_level,
                "prep_content": reply,
                "timestamp": datetime.now()
            })
        except Exception as e:
            print(f"Error saving interview prep: {e}")
        
        return jsonify({"interview_prep": reply})
    else:
        return jsonify({"error": "Interview prep generation failed"}), 500

@app.route('/ai_skill_analyzer', methods=['POST'])
def ai_skill_analyzer():
    data = request.get_json()
    skills_text = data.get("skills", "")
    career_goal = data.get("career_goal", "")
    user_email = data.get("email", "anonymous")
    
    if not skills_text:
        return jsonify({"error": "Skills description required"}), 400
    
    skill_analysis_prompt = f"""
    You are a career development expert analyzing skills for a Kenyan professional.
    
    Current Skills: {skills_text}
    Career Goal: {career_goal}
    
    Provide:
    1. Skills Gap Analysis
    2. Missing Skills for Career Goal
    3. Skill Development Roadmap
    4. Recommended Courses/Training in Kenya
    5. Online Learning Resources
    6. Certification Recommendations
    7. Timeline for Skill Development
    8. Networking Opportunities
    
    Focus on practical, actionable steps.
    """
    
    messages = [
        {"role": "system", "content": "You are a career development expert specializing in skill analysis and development."},
        {"role": "user", "content": skill_analysis_prompt}
    ]
    
    reply = ask_ai(messages, max_tokens=1200)
    
    if reply:
        # Save skill analysis to Firebase
        try:
            db.collection("skill_analyses").add({
                "user": user_email,
                "email": user_email,
                "skills": skills_text,
                "career_goal": career_goal,
                "analysis_result": reply,
                "timestamp": datetime.now()
            })
        except Exception as e:
            print(f"Error saving skill analysis: {e}")
        
        return jsonify({"skill_analysis": reply})
    else:
        return jsonify({"error": "Skill analysis generation failed"}), 500

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", cbc_explainer=CBC_SUMMARY, firebase_config=FIREBASE_CONFIG)

# ========== M-Pesa Payment Routes ==========

@app.route('/api/subscription/plans')
def get_subscription_plans():
    """Get all available subscription plans"""
    try:
        plans = subscription_manager.get_all_plans()
        return jsonify({"plans": plans})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/subscription/status')
def get_subscription_status():
    """Check user's subscription status"""
    try:
        user_id = request.args.get('user_id')
        if not user_id:
            return jsonify({"error": "User ID required"}), 400
        
        status = subscription_manager.check_subscription_status(user_id)
        return jsonify(status)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/payment/initiate', methods=['POST'])
def initiate_payment():
    """Initiate M-Pesa STK Push payment"""
    try:
        data = request.get_json()
        phone_number = data.get('phone_number')
        plan_type = data.get('plan_type')
        user_id = data.get('user_id')
        
        if not all([phone_number, plan_type, user_id]):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Get plan details
        plan = subscription_manager.get_plan_details(plan_type)
        if not plan:
            return jsonify({"error": "Invalid plan type"}), 400
        
        # Generate unique account reference
        account_reference = f"CAREERMENTOR_{user_id}_{int(datetime.now().timestamp())}"
        
        # Initiate STK Push
        result = mpesa.initiate_stk_push(
            phone_number=phone_number,
            amount=plan['price'],
            account_reference=account_reference,
            transaction_desc=f"CareerMentor {plan['name']} Subscription"
        )
        
        if 'error' in result:
            return jsonify(result), 500
        
        # Store payment request for tracking
        checkout_request_id = result.get('CheckoutRequestID')
        if checkout_request_id:
            db.collection("payment_requests").add({
                "user_id": user_id,
                "plan_type": plan_type,
                "checkout_request_id": checkout_request_id,
                "account_reference": account_reference,
                "amount": plan['price'],
                "phone_number": phone_number,
                "status": "pending",
                "created_at": datetime.now()
            })
        
        return jsonify({
            "success": True,
            "message": "Payment request sent to your phone. Please complete the payment on your M-Pesa menu.",
            "checkout_request_id": checkout_request_id
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/payment/status', methods=['POST'])
def check_payment_status():
    """Check payment status"""
    try:
        data = request.get_json()
        checkout_request_id = data.get('checkout_request_id')
        
        if not checkout_request_id:
            return jsonify({"error": "Checkout request ID required"}), 400
        
        # Query M-Pesa for payment status
        result = mpesa.query_stk_push_status(checkout_request_id)
        
        if 'error' in result:
            return jsonify(result), 500
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/mpesa/callback', methods=['POST'])
def mpesa_callback():
    """Handle M-Pesa payment callback"""
    try:
        callback_data = request.get_json()
        
        # Process callback
        result = mpesa.process_callback(callback_data)
        
        if result.get('success'):
            # Payment successful - create subscription
            checkout_request_id = result['checkout_request_id']
            
            # Find the payment request
            payment_requests = db.collection("payment_requests").where("checkout_request_id", "==", checkout_request_id).stream()
            
            for payment_request in payment_requests:
                payment_data = payment_request.to_dict()
                
                # Create subscription
                subscription_result = subscription_manager.create_subscription(
                    user_id=payment_data['user_id'],
                    plan_type=payment_data['plan_type'],
                    payment_reference=result['mpesa_receipt_number']
                )
                
                if subscription_result.get('success'):
                    # Update payment request status
                    db.collection("payment_requests").document(payment_request.id).update({
                        "status": "completed",
                        "mpesa_receipt_number": result['mpesa_receipt_number'],
                        "completed_at": datetime.now()
                    })
                    
                    print(f"Subscription created successfully for user {payment_data['user_id']}")
                else:
                    print(f"Failed to create subscription: {subscription_result}")
        
        return jsonify({"status": "received"})
        
    except Exception as e:
        print(f"Error processing M-Pesa callback: {e}")
        return jsonify({"error": str(e)}), 500

# ========== Admin Routes ==========

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin_login.html', error='Invalid credentials')
    
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/admin')
@admin_required
def admin_dashboard():
    return render_template("admin.html")

@app.route('/admin/api/stats')
@admin_required
def get_stats():
    try:
        # Get user count
        users = db.collection("users").stream()
        user_count = len(list(users))
        
        # Get message count
        messages = db.collection("messages").stream()
        message_count = len(list(messages))
        
        # Get CV downloads count
        cv_downloads = db.collection("cv_downloads").stream()
        cv_count = len(list(cv_downloads))
        
        # Get pathway downloads count
        pathway_downloads = db.collection("pathway_downloads").stream()
        pathway_count = len(list(pathway_downloads))
        
        # Get daily stats for the last 7 days
        today = datetime.now()
        daily_stats = []
        for i in range(7):
            date = today - timedelta(days=i)
            start_of_day = datetime.combine(date.date(), datetime.min.time())
            end_of_day = datetime.combine(date.date(), datetime.max.time())
            
            # Count messages for this day
            daily_messages = db.collection("messages").where("timestamp", ">=", start_of_day).where("timestamp", "<=", end_of_day).stream()
            daily_message_count = len(list(daily_messages))
            
            # Count CV downloads for this day
            daily_cvs = db.collection("cv_downloads").where("timestamp", ">=", start_of_day).where("timestamp", "<=", end_of_day).stream()
            daily_cv_count = len(list(daily_cvs))
            
            daily_stats.append({
                "date": date.strftime("%Y-%m-%d"),
                "messages": daily_message_count,
                "cvs": daily_cv_count
            })
        
        return jsonify({
            "users": user_count,
            "messages": message_count,
            "cvs": cv_count,
            "pathways": pathway_count,
            "daily_stats": daily_stats
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/admin/api/users')
@admin_required
def get_users():
    try:
        users = []
        user_docs = db.collection("users").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(100).stream()
        for user_doc in user_docs:
            data = user_doc.to_dict()
            users.append({
                "id": user_doc.id,
                "name": data.get("name", "Unknown"),
                "email": data.get("email", "No email"),
                "provider": data.get("provider", "email"),
                "timestamp": data.get("timestamp").strftime("%Y-%m-%d %H:%M") if data.get("timestamp") else "Unknown"
            })
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/admin/api/messages')
@admin_required
def get_messages():
    try:
        logs = []
        messages = db.collection("messages").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(100).stream()
        for msg in messages:
            data = msg.to_dict()
            logs.append({
                "id": msg.id,
                "user": data.get("user", "anonymous"),
                "email": data.get("email", "No email"),
                "question": data.get("user_message", "No question"),
                "reply": data.get("ai_reply", "No reply"),
                "timestamp": data.get("timestamp").strftime("%Y-%m-%d %H:%M") if data.get("timestamp") else "Unknown"
            })
        return jsonify(logs)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/admin/api/cv_downloads')
@admin_required
def get_cvs():
    try:
        logs = []
        entries = db.collection("cv_downloads").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(100).stream()
        for entry in entries:
            data = entry.to_dict()
            logs.append({
                "id": entry.id,
                "name": data.get("name", "Unknown"),
                "email": data.get("email", "No email"),
                "timestamp": data.get("timestamp").strftime("%Y-%m-%d %H:%M") if data.get("timestamp") else "Unknown"
            })
        return jsonify(logs)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/admin/api/pathway_downloads')
@admin_required
def get_pathway_downloads():
    try:
        logs = []
        entries = db.collection("pathway_downloads").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(100).stream()
        for entry in entries:
            data = entry.to_dict()
            logs.append({
                "id": entry.id,
                "name": data.get("name", "Unknown"),
                "email": data.get("email", "No email"),
                "prompt": data.get("prompt", "No prompt"),
                "timestamp": data.get("timestamp").strftime("%Y-%m-%d %H:%M") if data.get("timestamp") else "Unknown"
            })
        return jsonify(logs)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

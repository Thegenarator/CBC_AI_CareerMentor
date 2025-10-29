from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore, auth
import os
from datetime import datetime, timedelta
import json

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

# Firebase setup (assumes already initialized)
db = firestore.client()

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
    app.run(debug=True, port=5001)

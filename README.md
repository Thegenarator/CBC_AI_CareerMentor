# AI CareerMentor Kenya 🇰🇪

<div align="center">
  <img src="https://img.shields.io/badge/Python-Flask-blue" alt="Python Flask">
  <img src="https://img.shields.io/badge/AI-OpenAI-green" alt="OpenAI">
  <img src="https://img.shields.io/badge/Database-Firebase-orange" alt="Firebase">
  <img src="https://img.shields.io/badge/Payments-M--Pesa-yellow" alt="M-Pesa">
  <img src="https://img.shields.io/badge/UI-TailwindCSS-purple" alt="TailwindCSS">
</div>

<div align="center">
  <h3>🚀 Your Complete AI-Powered Career Guidance Platform</h3>
  <p>Empowering Kenyan students with personalized career guidance, CBC pathway recommendations, and professional development tools.</p>
</div>

---

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📸 Screenshots](#-screenshots)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Detailed Setup](#️-detailed-setup)
- [🎮 User Guide](#-user-guide)
- [💳 Payment Integration](#-payment-integration)
- [🔧 Configuration](#-configuration)
- [📱 Mobile Experience](#-mobile-experience)
- [🎓 Premium Features](#-premium-features)
- [👨‍💼 Admin Panel](#-admin-panel)
- [🚀 Deployment](#-deployment)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🎯 Overview

**AI CareerMentor Kenya** is a comprehensive career guidance platform specifically designed for Kenyan students navigating the Competency-Based Curriculum (CBC). Our AI-powered system provides personalized career advice, CBC pathway recommendations, professional CV generation, and advanced career development tools.

### 🎯 Target Audience
- **High School Students** (Form 1-4)
- **CBC Students** (Grade 4-12)
- **University Students**
- **Job Seekers**
- **Career Changers**
- **Parents and Guardians**

---

## ✨ Features

### 🆓 **Free Features**
- **AI Career Chatbot** - Ask questions about CBC, careers, and education
- **CV Generator** - Create professional CVs with AI assistance
- **CBC Pathway Explorer** - Discover suitable Senior School pathways
- **User Dashboard** - Track your progress and activities
- **Firebase Authentication** - Secure login with Google or email

### 💎 **Premium Features**
- **AI Career Assessment** - Comprehensive personality and career analysis
- **AI Interview Preparation** - Job-specific interview coaching
- **AI Skill Analyzer** - Skills gap analysis and development roadmap
- **Advanced Analytics** - Detailed progress tracking
- **Priority Support** - Enhanced customer service

### 💰 **Monetization**
- **M-Pesa Integration** - Seamless mobile payments
- **Subscription Plans** - Basic (KSh 300), Premium (KSh 500), Professional (KSh 1,000)
- **Pay-per-use** options available

---

## 🛠️ Tech Stack

### **Backend**
- **Python 3.8+** - Core programming language
- **Flask** - Web framework
- **Firebase Admin SDK** - Database and authentication
- **OpenAI GPT-3.5** - AI language model
- **Groq API** - Fast AI responses (fallback)
- **M-Pesa API** - Payment processing

### **Frontend**
- **HTML5** - Structure
- **Tailwind CSS** - Styling and responsive design
- **JavaScript (ES6+)** - Interactive functionality
- **Firebase SDK** - Client-side authentication
- **Font Awesome** - Icons

### **Database & Storage**
- **Firebase Firestore** - NoSQL database
- **Firebase Authentication** - User management
- **Firebase Storage** - File storage

### **Payment Processing**
- **M-Pesa STK Push** - Mobile payments
- **Safaricom Developer Portal** - API integration

---

## 📸 Screenshots

### 🏠 **Landing Page**
```
┌─────────────────────────────────────────────────────────┐
│  🎓 AI CareerMentor Kenya                              │
│                                                         │
│  Your CBC Journey Starts Here                          │
│  Discover your potential with AI-powered career        │
│  guidance, personalized CBC pathway recommendations,    │
│  and professional CV generation.                        │
│                                                         │
│  [🚀 Get Started Free] [▶️ Learn More]                 │
│                                                         │
│  ✨ Features:                                           │
│  • AI Career Mentor                                    │
│  • AI CV Generator                                     │
│  • CBC Pathway Guide                                   │
│  • Premium AI Tools                                    │
└─────────────────────────────────────────────────────────┘
```

### 📊 **Dashboard**
```
┌─────────────────────────────────────────────────────────┐
│  👤 Welcome, John Doe                    [🚪 Logout]   │
│                                                         │
│  📈 Quick Stats:                                       │
│  ┌─────────┬─────────┬─────────┐                       │
│  │ AI Chat │ CVs Gen │ Pathways│                       │
│  │   12    │    3    │    2    │                       │
│  └─────────┴─────────┴─────────┘                       │
│                                                         │
│  🤖 AI Career Mentor                                   │
│  ┌─────────────────────────────────────────────────┐   │
│  │ Hi! Ask me anything about CBC or careers!       │   │
│  │ [Type your question...] [📤 Send]               │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  📄 AI CV Generator                                     │
│  📋 CBC Career Pathway Explorer                         │
│  💎 Premium AI Career Tools                             │
└─────────────────────────────────────────────────────────┘
```

### 💎 **Premium Features**
```
┌─────────────────────────────────────────────────────────┐
│  💎 Premium AI Career Tools                             │
│                                                         │
│  ┌─────────────┬─────────────┬─────────────┐           │
│  │🧠 Assessment│🤝 Interview │📊 Skill     │           │
│  │             │   Prep      │   Analyzer  │           │
│  │10 Questions │Job-specific │Gap Analysis │           │
│  │Personality  │STAR Method  │Roadmap      │           │
│  │Analysis     │Tips         │Courses      │           │
│  │             │             │             │           │
│  │[Start Test] │[Prepare]    │[Analyze]    │           │
│  └─────────────┴─────────────┴─────────────┘           │
│                                                         │
│  [👑 Subscribe to Premium]                              │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### **1. Prerequisites**
- Python 3.8 or higher
- Git
- Firebase account
- OpenAI API key
- M-Pesa developer account (optional)

### **2. Installation**
```bash
# Clone the repository
git clone https://github.com/yourusername/ai-careermentor-kenya.git
cd ai-careermentor-kenya

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### **3. Run the Application**
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## ⚙️ Detailed Setup

### **Step 1: Environment Configuration**

Create a `.env` file in the project root:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile

# Flask Configuration
SECRET_KEY=your_secret_key_change_this_in_production

# Admin Configuration
ADMIN_EMAIL=admin@careermentor.com
ADMIN_PASSWORD=admin123

# M-Pesa Configuration (Optional)
MPESA_CONSUMER_KEY=your_mpesa_consumer_key
MPESA_CONSUMER_SECRET=your_mpesa_consumer_secret
MPESA_BUSINESS_SHORTCODE=your_business_shortcode
MPESA_PASSKEY=your_mpesa_passkey
MPESA_CALLBACK_URL=https://your-domain.com/mpesa/callback
MPESA_ENVIRONMENT=sandbox
```

### **Step 2: Firebase Setup**

1. **Create Firebase Project**:
   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Create a new project
   - Enable Firestore Database
   - Enable Authentication

2. **Download Service Account**:
   - Go to Project Settings > Service Accounts
   - Generate new private key
   - Save as `firebase_config.json` in project root

3. **Configure Authentication**:
   - Enable Email/Password authentication
   - Enable Google authentication
   - Add your domain to authorized domains

### **Step 3: OpenAI Setup**

1. **Get API Key**:
   - Visit [OpenAI Platform](https://platform.openai.com/)
   - Create account and get API key
   - Add to `.env` file

2. **Optional - Groq Setup**:
   - Visit [Groq Console](https://console.groq.com/)
   - Get API key for faster responses
   - Add to `.env` file

---

## 🎮 User Guide

### **🏠 Landing Page Navigation**

1. **Header Section**:
   - **Logo**: Click to return to homepage
   - **Login/Register**: Access your account
   - **Google Sign-in**: Quick authentication

2. **Hero Section**:
   - **"Get Started Free"**: Redirects to dashboard
   - **"Learn More"**: Scrolls to features section

3. **Features Section**:
   - **AI Career Mentor**: Overview of chatbot
   - **CBC Expertise**: Curriculum knowledge
   - **Instant Results**: Speed and efficiency

4. **Premium Features Section**:
   - **AI Career Assessment**: Detailed description
   - **AI Interview Prep**: Interview coaching
   - **AI Skill Analyzer**: Skills development

5. **CBC Explanation**:
   - **Understanding CBC**: Curriculum overview
   - **Key Benefits**: Personalized learning paths

6. **CV Generator Section**:
   - **Try Our AI CV Generator**: Quick CV creation
   - **Text Area**: Describe yourself
   - **Generate Button**: Create CV preview
   - **Download PDF**: Get formatted CV

### **📊 Dashboard Navigation**

1. **Header**:
   - **User Name**: Shows logged-in user
   - **Logout Button**: Sign out securely

2. **Quick Stats Cards**:
   - **AI Conversations**: Number of chat interactions
   - **CVs Generated**: Number of CVs created
   - **Pathways Explored**: Number of pathway analyses

3. **AI Career Mentor Chat**:
   - **Chat Interface**: Real-time conversation
   - **Input Field**: Type your questions
   - **Send Button**: Submit your message
   - **Chat History**: Previous conversations

4. **CBC Information Panel**:
   - **About CBC**: Curriculum explanation
   - **Scrollable Content**: Detailed information

5. **AI CV Generator Section**:
   - **Form Fields**: Name, email, education, skills, interests
   - **Generate Button**: Create professional CV
   - **Status Messages**: Progress updates

6. **CBC Career Pathway Explorer**:
   - **Description Field**: Describe your interests
   - **Discover Button**: Generate pathway analysis
   - **Result Display**: Formatted pathway recommendations
   - **Download PDF**: Get pathway report

7. **Premium AI Career Tools**:
   - **Assessment Card**: Start career assessment
   - **Interview Prep Card**: Prepare for interviews
   - **Skill Analyzer Card**: Analyze your skills
   - **Subscribe Button**: Access premium features

### **💎 Premium Features Guide**

#### **🧠 AI Career Assessment**

1. **Access**: Click "Start Assessment" button
2. **Modal Opens**: 10 comprehensive questions
3. **Answer Questions**:
   - What activities do you enjoy most?
   - How do you prefer to learn?
   - What work environment appeals to you?
   - How do you handle challenges?
   - What motivates you most?
   - How do you work with others?
   - What subjects interest you?
   - How do you make decisions?
   - What are your strengths?
   - Where do you see yourself in 5 years?

4. **Submit**: Click "Get My Assessment"
5. **Results**: Comprehensive analysis including:
   - Personality Type Analysis (Big Five traits)
   - Learning Style Assessment
   - Career Interest Areas (Holland's RIASEC)
   - Strengths and Development Areas
   - Recommended CBC Pathways
   - Career Suggestions with salary expectations
   - Educational Roadmap
   - 2-Year Action Plan

#### **🤝 AI Interview Preparation**

1. **Access**: Click "Prepare for Interview" button
2. **Fill Form**:
   - **Job Title**: e.g., Software Developer, Marketing Manager
   - **Industry**: Technology, Healthcare, Finance, etc.
   - **Experience Level**: Entry, Mid, Senior

3. **Generate**: Click "Generate Interview Prep"
4. **Results**: Comprehensive guide including:
   - Common interview questions for the role
   - STAR method answers for behavioral questions
   - Industry-specific technical questions
   - Salary negotiation tips for Kenyan market
   - Company research suggestions
   - Follow-up email templates
   - Interview day checklist

#### **📊 AI Skill Analyzer**

1. **Access**: Click "Analyze Skills" button
2. **Fill Form**:
   - **Current Skills**: Describe your skills and experiences
   - **Career Goal**: e.g., Become a Data Scientist

3. **Analyze**: Click "Analyze My Skills"
4. **Results**: Detailed analysis including:
   - Skills Gap Analysis
   - Missing Skills for Career Goal
   - Skill Development Roadmap
   - Recommended Courses/Training in Kenya
   - Online Learning Resources
   - Certification Recommendations
   - Timeline for Skill Development
   - Networking Opportunities

### **💳 Payment Integration Guide**

#### **Subscription Plans**

1. **Basic Plan - KSh 300/month**:
   - 20 AI interactions/month
   - Basic CV generation
   - Pathway exploration
   - 1 premium feature/month

2. **Premium Plan - KSh 500/month**:
   - Unlimited AI interactions
   - All premium features
   - Priority support
   - Advanced analytics
   - PDF downloads

3. **Professional Plan - KSh 1,000/month**:
   - Everything in Premium
   - Bulk CV generation
   - Team management
   - Advanced analytics dashboard
   - API access

#### **Payment Process**

1. **Select Plan**: Choose subscription tier
2. **Enter Phone Number**: M-Pesa registered number
3. **Initiate Payment**: Click "Pay with M-Pesa"
4. **M-Pesa Prompt**: Complete payment on phone
5. **Confirmation**: Subscription activated
6. **Access**: Premium features unlocked

---

## 🔧 Configuration

### **Firebase Configuration**

1. **Firestore Rules**:
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if request.auth != null;
    }
  }
}
```

2. **Authentication Settings**:
   - Enable Email/Password
   - Enable Google Provider
   - Set authorized domains

### **M-Pesa Configuration**

1. **Sandbox Testing**:
   - Use test phone: `254708374149`
   - Test PIN: `0000`
   - Business Shortcode: `your_test_shortcode`

2. **Production Setup**:
   - Apply for production access
   - Get production credentials
   - Set up SSL certificate
   - Configure callback URL

---

## 📱 Mobile Experience

### **Responsive Design**
- **Mobile-First**: Optimized for smartphones
- **Touch-Friendly**: Large buttons and touch targets
- **Fast Loading**: Optimized for mobile networks
- **Offline Support**: Basic functionality without internet

### **Mobile Navigation**
1. **Hamburger Menu**: Collapsible navigation
2. **Swipe Gestures**: Natural mobile interactions
3. **Touch Feedback**: Visual feedback on touch
4. **Keyboard Optimization**: Mobile keyboard support

---

## 🎓 Premium Features

### **AI Career Assessment**
- **10 Comprehensive Questions**: Covering personality, learning style, interests
- **Big Five Personality Analysis**: Scientific personality assessment
- **Holland's RIASEC Model**: Career interest mapping
- **Learning Style Assessment**: Visual, auditory, kinesthetic preferences
- **CBC Pathway Recommendations**: Based on assessment results
- **Kenyan Salary Expectations**: Local market insights
- **2-Year Action Plan**: Specific steps for development

### **AI Interview Preparation**
- **Job-Specific Questions**: Tailored to role and industry
- **STAR Method Templates**: Structured answer format
- **Industry-Specific Technical Questions**: Role-relevant queries
- **Kenyan Salary Negotiation Tips**: Local market advice
- **Company Research Suggestions**: Preparation strategies
- **Follow-up Email Templates**: Post-interview communication
- **Interview Day Checklist**: Practical preparation steps

### **AI Skill Analyzer**
- **Skills Gap Analysis**: Current vs. required skills
- **Development Roadmap**: Step-by-step progression
- **Course Recommendations**: Local institutions and programs
- **Online Learning Resources**: Free and paid options
- **Certification Recommendations**: Kenyan market relevance
- **Timeline for Skill Development**: Realistic milestones
- **Networking Opportunities**: Local professional networks

---

## 👨‍💼 Admin Panel

### **Access**
- URL: `/admin`
- Login with admin credentials
- Secure session management

### **Features**
1. **Dashboard Overview**:
   - Total users count
   - Total messages count
   - CV downloads count
   - Pathway downloads count
   - Daily statistics (last 7 days)

2. **User Management**:
   - View all registered users
   - User details and registration dates
   - Authentication providers
   - Activity tracking

3. **Message Monitoring**:
   - All AI conversations
   - User questions and AI responses
   - Timestamp tracking
   - Search and filter capabilities

4. **Download Tracking**:
   - CV download history
   - Pathway report downloads
   - User activity patterns
   - Usage analytics

5. **Payment Monitoring**:
   - Subscription status
   - Payment history
   - Revenue tracking
   - User upgrade patterns

---

## 🚀 Deployment

### **Local Development**
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
python setup_env.py
# Edit .env with your keys

# Run development server
python app.py
```

### **💰 FREE Deployment Options** (Recommended!)

#### **🥇 Option 1: Render.com (Easiest - FREE Forever!)**
**Perfect for:** Quick deployment, zero configuration, free forever

- ✅ **FREE** - 750 hours/month forever
- ✅ **5 minute setup** - Just connect GitHub
- ✅ **Auto-deploy** from Git
- ✅ **Free SSL** certificate

**Quick Start:**
1. Sign up at https://render.com (free, no credit card)
2. Connect GitHub repository
3. Create Web Service
4. Add environment variables
5. Deploy! 🎉

**📖 Full Guide:** See [`render_deploy.md`](render_deploy.md) for detailed steps

**Your app will be at:** `https://your-app.onrender.com`

---

#### **🥈 Option 2: AWS EC2 Free Tier (Learn AWS)**
**Perfect for:** Learning AWS, understanding cloud infrastructure

- ✅ **FREE for first year** - 750 hours/month
- ✅ **t2.micro instance** - Free tier eligible
- ✅ **Full control** - Learn Linux/SSH/AWS

**Quick Start:**
1. Launch EC2 t2.micro instance
2. Run: `./deploy_ec2.sh`
3. Configure environment variables
4. Start service

**📖 Full Guide:** See [`FREE_TIER_DEPLOYMENT.md`](FREE_TIER_DEPLOYMENT.md) → AWS EC2 section

**Cost:** FREE (first year), then ~$7-10/month

---

#### **🥉 Option 3: Railway.app (Modern)**
**Perfect for:** Modern deployment platform

- ✅ **$5 free credit/month**
- ✅ **Easy GitHub integration**
- ✅ **Auto SSL**

**Quick Start:**
1. Sign up at https://railway.app
2. Deploy from GitHub
3. Add environment variables
4. Done!

**📖 Full Guide:** See [`FREE_TIER_DEPLOYMENT.md`](FREE_TIER_DEPLOYMENT.md) → Railway section

---

### **💵 Paid Deployment Options** (For Production Scale)

#### **Option 4: AWS Elastic Beanstalk**
- Automatic scaling and load balancing
- Built-in monitoring
- **Cost:** ~$25-35/month

**📖 Full Guide:** See [`AWS_DEPLOYMENT_GUIDE.md`](AWS_DEPLOYMENT_GUIDE.md) → Method 1

#### **Option 5: AWS EC2**
- Full control and customization
- **Cost:** ~$7-15/month (after free tier)

**📖 Full Guide:** See [`AWS_DEPLOYMENT_GUIDE.md`](AWS_DEPLOYMENT_GUIDE.md) → Method 2

---

### **📚 Deployment Documentation**

- **[FREE_TIER_QUICK_START.md](FREE_TIER_QUICK_START.md)** - ⚡ Quick reference for free deployment
- **[FREE_TIER_DEPLOYMENT.md](FREE_TIER_DEPLOYMENT.md)** - 📖 Complete free tier guide
- **[render_deploy.md](render_deploy.md)** - 🎯 Step-by-step Render.com guide
- **[AWS_DEPLOYMENT_GUIDE.md](AWS_DEPLOYMENT_GUIDE.md)** - 🚀 Comprehensive AWS guide
- **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)** - ✅ Pre-deployment checklist

---

### **Environment Variables for Production**

Set all these in your deployment platform:

```env
# Firebase
FIREBASE_API_KEY=your_firebase_api_key
FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_APP_ID=your_app_id

# AI Services
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key

# App Configuration
SECRET_KEY=your_strong_secret_key
ADMIN_EMAIL=admin@careermentor.com
ADMIN_PASSWORD=your_strong_password
FLASK_ENV=production

# M-Pesa (if using)
MPESA_CONSUMER_KEY=your_mpesa_key
MPESA_CONSUMER_SECRET=your_mpesa_secret
MPESA_BUSINESS_SHORTCODE=your_shortcode
MPESA_PASSKEY=your_passkey
MPESA_CALLBACK_URL=https://your-domain.com/mpesa/callback
MPESA_ENVIRONMENT=sandbox
```

**Plus:** Upload `firebase_config.json` to your server

---

### **🚀 Recommended: Start with FREE Tier!**

**New to deployment?** → Try **Render.com** (5 minutes, free forever)  
**Want to learn AWS?** → Try **AWS EC2 Free Tier** (free for first year)  
**Need scaling?** → Upgrade to **Elastic Beanstalk** later

---

## 🤝 Contributing

### **How to Contribute**
1. **Fork the Repository**
2. **Create Feature Branch**: `git checkout -b feature/amazing-feature`
3. **Commit Changes**: `git commit -m 'Add amazing feature'`
4. **Push to Branch**: `git push origin feature/amazing-feature`
5. **Open Pull Request**

### **Development Guidelines**
- Follow PEP 8 style guide
- Write comprehensive tests
- Update documentation
- Ensure mobile compatibility
- Test payment integration

### **Issue Reporting**
- Use GitHub Issues
- Provide detailed description
- Include screenshots if applicable
- Specify browser and device

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

### **Contact Information**
- **Email**: kibiwottkamoo@gmail.com
- **Phone**: +254 721 517 279
- **Website**: https://careermentor.co.ke

### **Documentation**
- **API Documentation**: `/docs/api`
- **User Guide**: `/docs/user-guide`
- **Developer Guide**: `/docs/developer-guide`

### **Community**
- **GitHub Discussions**: For questions and discussions
- **Discord Server**: Real-time community support
- **Twitter**: @CareerMentorKE

---

<div align="center">
  <h3>🚀 Ready to Transform Your Career Journey?</h3>
  <p>Join thousands of Kenyan students who are already discovering their potential with AI CareerMentor Kenya!</p>
  
  [![Get Started](https://img.shields.io/badge/Get%20Started-Free-brightgreen)](https://careermentor.co.ke)
  [![Documentation](https://img.shields.io/badge/Documentation-Read%20More-blue)](https://docs.careermentor.co.ke)
  [![Support](https://img.shields.io/badge/Support-Contact%20Us-orange)](mailto:support@careermentor.co.ke)
</div>

---

<div align="center">
  <p>Made with ❤️ for Kenyan Students</p>
  <p>© 2024 AI CareerMentor Kenya. All rights reserved.</p>
</div>

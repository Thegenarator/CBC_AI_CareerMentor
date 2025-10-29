# AI CareerMentor Kenya - Setup Guide

## 🚀 Quick Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- Git
- Firebase account
- OpenAI API key
- M-Pesa developer account (optional)

### 2. Installation Steps

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

### 3. Environment Configuration

Create a `.env` file in the project root with the following variables:

```env
# OpenAI Configuration (Required)
OPENAI_API_KEY=your_openai_api_key_here

# Groq Configuration (Optional)
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile

# Flask Configuration (Required)
SECRET_KEY=your_secret_key_change_this_in_production

# Admin Panel Configuration (Required)
ADMIN_EMAIL=admin@careermentor.com
ADMIN_PASSWORD=admin123

# M-Pesa Configuration (Optional)
MPESA_CONSUMER_KEY=your_mpesa_consumer_key
MPESA_CONSUMER_SECRET=your_mpesa_consumer_secret
MPESA_BUSINESS_SHORTCODE=174379
MPESA_PASSKEY=your_mpesa_passkey
MPESA_CALLBACK_URL=https://your-domain.com/mpesa/callback
MPESA_ENVIRONMENT=sandbox

# Application Settings
FLASK_ENV=development
APP_URL=http://localhost:5000
```

### 4. Firebase Setup

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

### 5. OpenAI Setup

1. **Get API Key**:
   - Visit [OpenAI Platform](https://platform.openai.com/)
   - Create account and get API key
   - Add to `.env` file

2. **Optional - Groq Setup**:
   - Visit [Groq Console](https://console.groq.com/)
   - Get API key for faster responses
   - Add to `.env` file

### 6. Run the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## 🔧 Configuration Details

### Firebase Configuration

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

### M-Pesa Configuration

1. **Sandbox Testing**:
   - Use test phone: `254708374149`
   - Test PIN: `0000`
   - Business Shortcode: `174379`

2. **Production Setup**:
   - Apply for production access
   - Get production credentials
   - Set up SSL certificate
   - Configure callback URL

## 🚀 Deployment Options

### Heroku Deployment

```bash
# Install Heroku CLI
# Create Procfile
echo "web: python app.py" > Procfile

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### DigitalOcean Deployment

```bash
# Set up Ubuntu server
# Install Python and dependencies
# Configure nginx
# Set up SSL certificate
# Deploy application
```

### AWS Deployment

```bash
# Use Elastic Beanstalk
# Configure environment
# Deploy application
# Set up RDS for database
# Configure CloudFront for CDN
```

## 📱 Mobile Configuration

The application is mobile-responsive and works on:
- iOS Safari
- Android Chrome
- Mobile browsers
- Progressive Web App (PWA) support

## 🔒 Security Considerations

1. **Environment Variables**: Never commit `.env` file to version control
2. **API Keys**: Keep API keys secure and rotate regularly
3. **Firebase Rules**: Configure proper Firestore security rules
4. **HTTPS**: Enable HTTPS in production
5. **Rate Limiting**: Implement rate limiting for API endpoints

## 🐛 Troubleshooting

### Common Issues

1. **Firebase Connection Error**:
   - Check `firebase_config.json` file
   - Verify project ID and credentials
   - Ensure Firestore is enabled

2. **OpenAI API Error**:
   - Verify API key is correct
   - Check API usage limits
   - Ensure sufficient credits

3. **M-Pesa Integration Issues**:
   - Verify consumer key and secret
   - Check business shortcode
   - Ensure callback URL is accessible

4. **Authentication Issues**:
   - Check Firebase authentication settings
   - Verify authorized domains
   - Clear browser cache

### Debug Mode

Enable debug mode by setting:
```env
DEBUG=True
FLASK_ENV=development
```

## 📞 Support

For additional help:
- Email: support@careermentor.co.ke
- GitHub Issues: Report bugs and feature requests
- Documentation: Check the main README.md

## 🎯 Next Steps

After setup:
1. Test all features
2. Configure M-Pesa payments
3. Set up analytics
4. Deploy to production
5. Monitor usage and performance

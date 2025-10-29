# Environment Variables Configuration Guide

## Required Environment Variables

Create a `.env` file in your project root with the following variables:

### OpenAI Configuration
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Groq Configuration (Optional)
```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

### Flask Configuration
```env
SECRET_KEY=your_secret_key_change_this_in_production
```

### Admin Panel Configuration
```env
ADMIN_EMAIL=admin@careermentor.com
ADMIN_PASSWORD=admin123
```

### Firebase Configuration
```env
FIREBASE_API_KEY=your_firebase_api_key
FIREBASE_AUTH_DOMAIN=your_project_id.firebaseapp.com
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_APP_ID=your_app_id
```

### M-Pesa Configuration (Optional)
```env
MPESA_CONSUMER_KEY=your_mpesa_consumer_key
MPESA_CONSUMER_SECRET=your_mpesa_consumer_secret
MPESA_BUSINESS_SHORTCODE=your_business_shortcode
MPESA_PASSKEY=your_mpesa_passkey
MPESA_CALLBACK_URL=https://your-domain.com/mpesa/callback
MPESA_ENVIRONMENT=sandbox
```

### Application Settings
```env
FLASK_ENV=development
APP_URL=http://localhost:5000
```

## How to Get Your API Keys

### Firebase
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project
3. Go to Project Settings > General > Your apps
4. Copy the configuration values

### OpenAI
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Go to API Keys section
3. Create a new API key

### M-Pesa
1. Visit [Safaricom Developer Portal](https://developer.safaricom.co.ke/)
2. Create an account and app
3. Get your consumer key and secret

## Security Notes

- Never commit your `.env` file to version control
- Use different keys for development and production
- Rotate your API keys regularly
- Keep your keys secure and private

#!/usr/bin/env python3
"""
Environment Setup Script for AI CareerMentor Kenya
This script helps you create a .env file with the necessary configuration.
"""

import os

def create_env_file():
    """Create a .env file with Firebase configuration"""
    
    env_content = """# AI CareerMentor Kenya - Environment Configuration
# Firebase Configuration
FIREBASE_API_KEY=AIzaSyDTm-ckLXcOcRM_4g5hTs94Tm4W_BUx-eI
FIREBASE_AUTH_DOMAIN=cbch-6178c.firebaseapp.com
FIREBASE_PROJECT_ID=cbch-6178c
FIREBASE_APP_ID=1:577618974847:web:730ae29830d14fc0a6c74a

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Groq Configuration (Optional)
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile

# Flask Configuration
SECRET_KEY=your_secret_key_change_this_in_production

# Admin Panel Configuration
ADMIN_EMAIL=admin@careermentor.com
ADMIN_PASSWORD=admin123

# M-Pesa Configuration (Optional)
MPESA_CONSUMER_KEY=GnMdAhLo9w1oGUApZpWh9myVB0G35tTqchfkKAdhtmifCeoK
MPESA_CONSUMER_SECRET=Pr1n6TFKcMqj7iYkVfA7HnvQAnUeYO2MBcx8SbGScVyQAGDXOSADiInJ7gGdxtpD
MPESA_BUSINESS_SHORTCODE=174379
MPESA_PASSKEY=your_mpesa_passkey
MPESA_CALLBACK_URL=https://your-domain.com/mpesa/callback
MPESA_ENVIRONMENT=sandbox

# Application Settings
FLASK_ENV=development
APP_URL=http://localhost:5000
"""
    
    if os.path.exists('.env'):
        print("⚠️  .env file already exists!")
        response = input("Do you want to overwrite it? (y/N): ")
        if response.lower() != 'y':
            print("❌ Cancelled. .env file not modified.")
            return
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ .env file created successfully!")
        print("📝 Please update the following values:")
        print("   - OPENAI_API_KEY: Get from https://platform.openai.com/api-keys")
        print("   - SECRET_KEY: Generate a secure random string")
        print("   - MPESA_PASSKEY: Get from Safaricom Developer Portal")
        print("   - Other optional values as needed")
        
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")

if __name__ == "__main__":
    print("🚀 AI CareerMentor Kenya - Environment Setup")
    print("=" * 50)
    create_env_file()

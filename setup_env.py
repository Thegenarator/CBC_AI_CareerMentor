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
FIREBASE_API_KEY=your_firebase_api_key_here
FIREBASE_AUTH_DOMAIN=your_project_id.firebaseapp.com
FIREBASE_PROJECT_ID=your_project_id_here
FIREBASE_APP_ID=your_app_id_here

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
MPESA_CONSUMER_KEY=your_mpesa_consumer_key_here
MPESA_CONSUMER_SECRET=your_mpesa_consumer_secret_here
MPESA_BUSINESS_SHORTCODE=your_business_shortcode_here
MPESA_PASSKEY=your_mpesa_passkey_here
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
        print("📝 Please update the following values with your actual credentials:")
        print("   - FIREBASE_API_KEY: Get from Firebase Console > Project Settings > General > Your apps")
        print("   - FIREBASE_AUTH_DOMAIN: Usually project-id.firebaseapp.com")
        print("   - FIREBASE_PROJECT_ID: Your Firebase project ID")
        print("   - FIREBASE_APP_ID: Get from Firebase Console")
        print("   - OPENAI_API_KEY: Get from https://platform.openai.com/api-keys")
        print("   - SECRET_KEY: Generate a secure random string")
        print("   - MPESA_CONSUMER_KEY: Get from Safaricom Developer Portal")
        print("   - MPESA_CONSUMER_SECRET: Get from Safaricom Developer Portal")
        print("   - MPESA_BUSINESS_SHORTCODE: Your M-Pesa business shortcode")
        print("   - MPESA_PASSKEY: Get from Safaricom Developer Portal")
        
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")

if __name__ == "__main__":
    print("🚀 AI CareerMentor Kenya - Environment Setup")
    print("=" * 50)
    create_env_file()

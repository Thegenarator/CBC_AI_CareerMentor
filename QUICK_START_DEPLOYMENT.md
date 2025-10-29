# 🚀 Quick Start - AWS Deployment

This is a simplified guide to get you started quickly. For detailed instructions, see `AWS_DEPLOYMENT_GUIDE.md`.

## Option 1: Elastic Beanstalk (Easiest - 15 minutes)

### Prerequisites
```bash
pip install awsebcli --upgrade --user
```

### Deploy Steps

1. **Initialize EB**
```bash
cd C:\Users\MK\Desktop\Cbc_AI
eb init -p python-3.9 cbch-careermentor
# Choose region: us-east-1 (or your preferred)
```

2. **Create Environment**
```bash
eb create cbch-production
# Wait 5-10 minutes for setup
```

3. **Set Environment Variables**
```bash
# Copy all variables from your .env file
eb setenv FIREBASE_API_KEY="your_key" FIREBASE_AUTH_DOMAIN="your_domain" FIREBASE_PROJECT_ID="your_id" FIREBASE_APP_ID="your_app_id" OPENAI_API_KEY="your_key" GROQ_API_KEY="your_key" SECRET_KEY="your_secret" ADMIN_EMAIL="admin@careermentor.com" ADMIN_PASSWORD="your_password" MPESA_CONSUMER_KEY="your_key" MPESA_CONSUMER_SECRET="your_secret" MPESA_BUSINESS_SHORTCODE="your_shortcode" MPESA_PASSKEY="your_passkey" MPESA_CALLBACK_URL="https://your-app.elasticbeanstalk.com/mpesa/callback" FLASK_ENV="production"
```

4. **Deploy**
```bash
eb deploy
```

5. **Open**
```bash
eb open
```

**Done!** 🎉

---

## Option 2: EC2 (More Control)

### Quick Steps

1. **Launch EC2 Instance**
   - AWS Console > EC2 > Launch Instance
   - Choose: Amazon Linux 2023
   - Type: t3.micro
   - Security Group: HTTP (80), HTTPS (443), SSH (22)

2. **Connect**
```bash
ssh -i your-key.pem ec2-user@your-ec2-ip
```

3. **Deploy**
```bash
git clone https://github.com/Thegenarator/CBC_AI_CareerMentor.git
cd CBC_AI_CareerMentor
chmod +x deploy_ec2.sh
./deploy_ec2.sh
```

4. **Configure**
```bash
cd /var/www/cbc_ai
# Copy your .env file content
nano .env
# Paste all environment variables

# Copy firebase_config.json
# Use SCP from local machine or create via nano
```

5. **Start**
```bash
sudo systemctl start cbc-ai
sudo systemctl status cbc-ai
```

**Done!** 🎉

---

## 🔧 Common Issues

### "Application failed to start"
→ Check logs: `eb logs` or `sudo journalctl -u cbc-ai -f`
→ Verify all environment variables are set
→ Check Firebase config is uploaded

### "Cannot connect to Firebase"
→ Verify `firebase_config.json` exists in app directory
→ Check Firebase environment variables

### "502 Bad Gateway"
→ Application not running
→ Check if service is active: `sudo systemctl status cbc-ai`

---

## 📝 Before Deploying - Checklist

- [ ] All API keys ready
- [ ] `.env` file prepared locally
- [ ] `firebase_config.json` ready
- [ ] M-Pesa callback URL updated to production URL
- [ ] Domain name ready (optional)

---

**Need detailed help?** See `AWS_DEPLOYMENT_GUIDE.md` for step-by-step instructions with screenshots and troubleshooting.


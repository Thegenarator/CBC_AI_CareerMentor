# 🚀 AWS Deployment Guide - AI CareerMentor Kenya

This comprehensive guide will walk you through deploying your Flask application on AWS. We'll cover two methods:
1. **AWS Elastic Beanstalk** (Recommended for beginners - easier)
2. **AWS EC2** (More control - better for learning)

---

## 📋 Prerequisites

Before starting, make sure you have:
- ✅ AWS Account (sign up at https://aws.amazon.com)
- ✅ AWS CLI installed (download from https://aws.amazon.com/cli/)
- ✅ Git installed
- ✅ All your API keys ready (.env file prepared)
- ✅ Firebase service account key (`firebase_config.json`)

---

## 🎯 Method 1: AWS Elastic Beanstalk (Recommended)

### Why Elastic Beanstalk?
- ✅ Easy to set up and deploy
- ✅ Automatic scaling and load balancing
- ✅ Built-in monitoring
- ✅ Handles SSL certificates
- ✅ Perfect for learning AWS

### Step-by-Step Deployment

#### Step 1: Install EB CLI

```bash
# On Windows (PowerShell)
pip install awsebcli --upgrade --user

# Verify installation
eb --version
```

#### Step 2: Prepare Your Project

Make sure your project structure looks like this:
```
Cbc_AI/
├── application.py          # WSGI entry point
├── app.py                  # Your Flask app
├── requirements.txt        # Python dependencies
├── .ebextensions/         # EB configuration (optional)
│   ├── 01_python.config
│   └── 02_nginx.config
├── static/                # Static files
├── templates/             # HTML templates
├── firebase_config.json    # Firebase credentials
└── .env                    # Environment variables (will be set in EB)
```

#### Step 3: Initialize Elastic Beanstalk

```bash
# Navigate to your project directory
cd C:\Users\MK\Desktop\Cbc_AI

# Initialize EB (choose your region, e.g., us-east-1)
eb init -p python-3.9 cbch-careermentor

# Follow the prompts:
# - Select region (e.g., us-east-1)
# - Create new application
# - Application name: cbch-careermentor
```

#### Step 4: Create Environment

```bash
# Create a production environment
eb create cbch-production

# This will take 5-10 minutes to:
# - Launch EC2 instance
# - Set up load balancer
# - Configure security groups
# - Deploy your application
```

#### Step 5: Configure Environment Variables

**Important:** Set all your API keys as environment variables:

```bash
# Set environment variables one by one
eb setenv FIREBASE_API_KEY="your_firebase_api_key"
eb setenv FIREBASE_AUTH_DOMAIN="your_project.firebaseapp.com"
eb setenv FIREBASE_PROJECT_ID="your_project_id"
eb setenv FIREBASE_APP_ID="your_app_id"
eb setenv OPENAI_API_KEY="your_openai_key"
eb setenv GROQ_API_KEY="your_groq_key"
eb setenv SECRET_KEY="your_secret_key_here"
eb setenv ADMIN_EMAIL="admin@careermentor.com"
eb setenv ADMIN_PASSWORD="your_admin_password"
eb setenv MPESA_CONSUMER_KEY="your_mpesa_key"
eb setenv MPESA_CONSUMER_SECRET="your_mpesa_secret"
eb setenv MPESA_BUSINESS_SHORTCODE="your_shortcode"
eb setenv MPESA_PASSKEY="your_passkey"
eb setenv MPESA_CALLBACK_URL="https://your-domain.elasticbeanstalk.com/mpesa/callback"
eb setenv MPESA_ENVIRONMENT="sandbox"
eb setenv FLASK_ENV="production"

# Or set all at once (PowerShell):
$env_vars = @"
FIREBASE_API_KEY=your_firebase_api_key
FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_APP_ID=your_app_id
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
SECRET_KEY=your_secret_key
ADMIN_EMAIL=admin@careermentor.com
ADMIN_PASSWORD=your_admin_password
MPESA_CONSUMER_KEY=your_mpesa_key
MPESA_CONSUMER_SECRET=your_mpesa_secret
MPESA_BUSINESS_SHORTCODE=your_shortcode
MPESA_PASSKEY=your_passkey
MPESA_CALLBACK_URL=https://your-domain.elasticbeanstalk.com/mpesa/callback
MPESA_ENVIRONMENT=sandbox
FLASK_ENV=production
"@
# Note: Use eb setenv for each variable separately, as above
```

#### Step 6: Upload Firebase Config File

```bash
# Create .ebextensions/03_files.config
```

Then use EB console or modify the deployment:

```bash
# Option 1: Use EB console
# Go to AWS Console > Elastic Beanstalk > Your environment > Configuration > Software
# Add a file system path or use environment property

# Option 2: Include in deployment package
# Make sure firebase_config.json is in your project root
```

Create `.ebextensions/03_firebase.config`:

```yaml
files:
  "/opt/python/current/app/firebase_config.json":
    mode: "000644"
    owner: webapp
    group: webapp
    content: |
      {
        "type": "service_account",
        "project_id": "your_project_id",
        "private_key_id": "your_private_key_id",
        "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
        "client_email": "your_client_email",
        "client_id": "your_client_id",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "your_cert_url"
      }
```

**Better approach:** Copy `firebase_config.json` content and paste into the file above, or upload via AWS Systems Manager Parameter Store.

#### Step 7: Deploy Your Application

```bash
# Deploy to production
eb deploy

# This will:
# - Package your application
# - Upload to S3
# - Deploy to EC2 instance
# - Restart the application
```

#### Step 8: Open Your Application

```bash
# Open in browser
eb open

# Or get the URL
eb status
```

#### Step 9: Monitor Your Application

```bash
# View logs
eb logs

# View status
eb status

# SSH into instance (if needed)
eb ssh
```

#### Step 10: Set Up Custom Domain (Optional)

1. Go to AWS Console > Elastic Beanstalk > Your Environment > Configuration
2. Click "Edit" on Load Balancer
3. Add a listener for HTTPS (port 443)
4. Upload your SSL certificate (use AWS Certificate Manager)

---

## 🖥️ Method 2: AWS EC2 (Advanced - More Learning)

### Why EC2?
- ✅ Full control over server
- ✅ Learn Linux administration
- ✅ More cost-effective for single instance
- ✅ Better understanding of infrastructure

### Step-by-Step Deployment

#### Step 1: Launch EC2 Instance

1. Go to AWS Console > EC2 > Launch Instance
2. Choose Amazon Linux 2023 AMI
3. Select instance type: t3.micro (free tier eligible)
4. Configure security group:
   - HTTP (80) from anywhere
   - HTTPS (443) from anywhere
   - SSH (22) from your IP
5. Launch and create/download key pair

#### Step 2: Connect to EC2 Instance

```bash
# On Windows, use PuTTY or WSL/Windows Terminal
# Convert .pem to .ppk using PuTTYgen if using PuTTY

# Or use SSH (if using WSL or Git Bash)
ssh -i your-key.pem ec2-user@your-ec2-ip
```

#### Step 3: Run Deployment Script

```bash
# Clone your repository
git clone https://github.com/Thegenarator/CBC_AI_CareerMentor.git
cd CBC_AI_CareerMentor

# Make deployment script executable
chmod +x deploy_ec2.sh

# Run deployment script
./deploy_ec2.sh
```

#### Step 4: Set Up Environment Variables

```bash
# Navigate to app directory
cd /var/www/cbc_ai

# Create .env file
nano .env

# Paste all your environment variables:
FIREBASE_API_KEY=your_key
FIREBASE_AUTH_DOMAIN=your_domain
# ... (all other variables)

# Save and exit (Ctrl+X, Y, Enter)
```

#### Step 5: Upload Firebase Config

```bash
# Use SCP to copy firebase_config.json
# From your local machine:
scp -i your-key.pem firebase_config.json ec2-user@your-ec2-ip:/var/www/cbc_ai/

# Or create it on the server
nano /var/www/cbc_ai/firebase_config.json
# Paste your Firebase service account JSON
```

#### Step 6: Start the Application

```bash
# Start the service
sudo systemctl start cbc-ai

# Check status
sudo systemctl status cbc-ai

# View logs
sudo journalctl -u cbc-ai -f
```

#### Step 7: Configure Domain (Optional)

1. Point your domain A record to EC2 instance IP
2. Set up SSL with Let's Encrypt:

```bash
# Install Certbot
sudo yum install -y certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

---

## 🔒 Security Checklist

- [ ] All API keys are in environment variables (not in code)
- [ ] `.env` file is in `.gitignore`
- [ ] `firebase_config.json` is in `.gitignore`
- [ ] HTTPS is enabled
- [ ] Admin credentials are strong
- [ ] Security groups only allow necessary ports
- [ ] Regular backups configured
- [ ] Monitoring and alerts set up

---

## 📊 Monitoring & Maintenance

### Elastic Beanstalk

```bash
# View application logs
eb logs

# Monitor metrics in AWS Console
# CloudWatch automatically tracks:
# - CPU usage
# - Request count
# - Response time
```

### EC2

```bash
# View application logs
sudo journalctl -u cbc-ai -f

# View system resources
htop
df -h
```

---

## 💰 Cost Estimation

### Elastic Beanstalk
- EC2 Instance: ~$7-15/month (t3.micro)
- Load Balancer: ~$16/month
- Data Transfer: ~$0.09/GB
- **Total: ~$25-35/month**

### EC2 (Single Instance)
- EC2 Instance: ~$7-15/month (t3.micro)
- Elastic IP: Free
- Data Transfer: ~$0.09/GB
- **Total: ~$7-15/month**

---

## 🐛 Troubleshooting

### Application Not Starting

```bash
# Check logs
eb logs  # For Elastic Beanstalk
sudo journalctl -u cbc-ai -f  # For EC2

# Check environment variables
eb printenv  # For Elastic Beanstalk
cat /var/www/cbc_ai/.env  # For EC2
```

### Cannot Connect to Firebase

- Verify `firebase_config.json` is uploaded correctly
- Check environment variables in EB console or `.env` file
- Ensure Firestore security rules allow your app

### M-Pesa Callbacks Not Working

- Update `MPESA_CALLBACK_URL` to your production URL
- Ensure your endpoint is accessible via HTTPS
- Check M-Pesa developer portal for callback logs

---

## 🚀 Next Steps After Deployment

1. Set up automatic deployments (CI/CD)
2. Configure auto-scaling
3. Set up monitoring alerts
4. Configure backups
5. Set up CDN for static files (CloudFront)
6. Enable CloudWatch logging

---

## 📚 Additional Resources

- [AWS Elastic Beanstalk Documentation](https://docs.aws.amazon.com/elasticbeanstalk/)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/2.3.x/deploying/)

---

## 🆘 Need Help?

If you encounter issues:
1. Check AWS CloudWatch logs
2. Review application logs (`eb logs` or `journalctl`)
3. Verify all environment variables are set
4. Check security group rules
5. Ensure `firebase_config.json` is correctly uploaded

**Let's deploy together!** 🎉


# 💰 Free Tier Deployment Guide

This guide covers **100% FREE** deployment options for your application. No credit card required (or very minimal usage).

---

## 🎯 Recommended: AWS EC2 Free Tier (First Year)

### Why This Is Free:
- ✅ **EC2 t2.micro**: 750 hours/month FREE (first 12 months)
- ✅ **Elastic IP**: Free (as long as instance is running)
- ✅ **Data Transfer**: 15 GB outbound FREE/month
- ✅ **Storage**: 8GB EBS volume FREE (first month, then ~$1/month)

**Total Cost: FREE for first year, then ~$7-10/month**

### Step-by-Step Free Deployment

#### Step 1: Create AWS Account
1. Go to https://aws.amazon.com
2. Click "Create an AWS Account"
3. Follow the signup process
4. **Note:** Credit card required but you won't be charged if you stay in free tier

#### Step 2: Launch EC2 Instance (Free Tier)

1. **Go to EC2 Console**
   - AWS Console → EC2 → Launch Instance

2. **Configure Instance:**
   - **Name:** `cbch-careermentor-free`
   - **AMI:** Amazon Linux 2023 AMI (Free Tier Eligible)
   - **Instance Type:** `t2.micro` (Free Tier Eligible)
   - **Key Pair:** Create new key pair, download `.pem` file
   - **Network Settings:**
     - Allow HTTP (port 80) from anywhere (0.0.0.0/0)
     - Allow HTTPS (port 443) from anywhere (0.0.0.0/0)
     - Allow SSH (port 22) from your IP only (for security)
   - **Storage:** 8 GB gp3 (Free Tier includes 30 GB EBS)

3. **Launch Instance**
   - Click "Launch Instance"
   - Wait for instance to be "Running"

#### Step 3: Allocate Elastic IP (Free)

1. EC2 Console → Elastic IPs → Allocate Elastic IP
2. Allocate new Elastic IP
3. Associate with your instance (this keeps IP free)

#### Step 4: Connect to Instance

**Windows (PowerShell or Git Bash):**
```bash
# Download your .pem key file
# Set permissions (if using Git Bash/WSL)
chmod 400 your-key.pem

# Connect
ssh -i your-key.pem ec2-user@YOUR_ELASTIC_IP
```

**Windows (PuTTY):**
1. Convert `.pem` to `.ppk` using PuTTYgen
2. Open PuTTY, enter your Elastic IP
3. Load converted `.ppk` key

#### Step 5: Install and Deploy (Automated)

```bash
# On EC2 instance, run:
cd ~
git clone https://github.com/Thegenarator/CBC_AI_CareerMentor.git
cd CBC_AI_CareerMentor

# Make deployment script executable
chmod +x deploy_ec2.sh

# Run deployment (this installs everything)
./deploy_ec2.sh
```

#### Step 6: Configure Environment

```bash
cd /var/www/cbc_ai

# Create .env file
nano .env
```

Paste all your environment variables (copy from local `.env` file):
```env
FIREBASE_API_KEY=your_key
FIREBASE_AUTH_DOMAIN=your_domain
FIREBASE_PROJECT_ID=your_id
FIREBASE_APP_ID=your_app_id
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
SECRET_KEY=your_secret_key
ADMIN_EMAIL=admin@careermentor.com
ADMIN_PASSWORD=your_password
MPESA_CONSUMER_KEY=your_key
MPESA_CONSUMER_SECRET=your_secret
MPESA_BUSINESS_SHORTCODE=your_shortcode
MPESA_PASSKEY=your_passkey
MPESA_CALLBACK_URL=http://YOUR_ELASTIC_IP/mpesa/callback
MPESA_ENVIRONMENT=sandbox
FLASK_ENV=production
```

**Save:** Ctrl+X, Y, Enter

#### Step 7: Upload Firebase Config

**Option A: Using SCP (from your local machine)**
```powershell
# In PowerShell or Git Bash
scp -i your-key.pem firebase_config.json ec2-user@YOUR_ELASTIC_IP:/var/www/cbc_ai/
```

**Option B: Create on Server**
```bash
nano /var/www/cbc_ai/firebase_config.json
# Paste your Firebase service account JSON
# Save: Ctrl+X, Y, Enter
```

#### Step 8: Start Application

```bash
# Start the service
sudo systemctl start cbc-ai

# Enable auto-start on boot
sudo systemctl enable cbc-ai

# Check status
sudo systemctl status cbc-ai

# View logs
sudo journalctl -u cbc-ai -f
```

#### Step 9: Access Your App

Open browser and go to: `http://YOUR_ELASTIC_IP`

**Done! Your app is live for FREE! 🎉**

---

## 🆓 Alternative: Render.com (Free Forever)

### Why Render?
- ✅ **Free tier forever** (no credit card required)
- ✅ **750 hours/month free** (enough for 24/7)
- ✅ **Auto-deploy from GitHub**
- ✅ **Free SSL certificate**
- ✅ **No AWS knowledge needed**

### Step-by-Step on Render

#### Step 1: Sign Up
1. Go to https://render.com
2. Sign up with GitHub (free)
3. Connect your GitHub account

#### Step 2: Deploy from GitHub

1. **New Web Service**
   - Dashboard → New → Web Service
   - Connect your repository: `CBC_AI_CareerMentor`

2. **Configure:**
   - **Name:** `cbch-careermentor`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn application:app --bind 0.0.0.0:$PORT`
   - **Plan:** Free (spinner instance)

3. **Environment Variables:**
   - Add all your environment variables:
     - `FIREBASE_API_KEY`
     - `FIREBASE_AUTH_DOMAIN`
     - `FIREBASE_PROJECT_ID`
     - `FIREBASE_APP_ID`
     - `OPENAI_API_KEY`
     - `GROQ_API_KEY`
     - `SECRET_KEY`
     - `ADMIN_EMAIL`
     - `ADMIN_PASSWORD`
     - All M-Pesa variables
     - `FLASK_ENV=production`

4. **Add Build Environment Variable:**
   - Add Firebase config as environment variable or use Shell Script:
   - Create file `firebase_config.json` in repo (add to `.gitignore` in local dev)

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (~5 minutes)
   - Your app will be at: `https://cbch-careermentor.onrender.com`

#### Step 3: Upload Firebase Config (Render)

Create a script to write Firebase config:

**Create `render_start.sh`:**
```bash
#!/bin/bash
# Write Firebase config from environment variable
echo "$FIREBASE_CONFIG_JSON" > firebase_config.json
# Start application
gunicorn application:app --bind 0.0.0.0:$PORT
```

Or use **Render Shell Script**:
1. Go to your service → Shell
2. Run:
```bash
echo '{"type":"service_account",...}' > firebase_config.json
```

**Or easier:** Add Firebase config as a file in your repo (encrypted) and load it.

---

## 🆓 Alternative: Railway.app (Free Tier)

### Why Railway?
- ✅ **$5 free credit/month** (enough for small apps)
- ✅ **Easy GitHub deployment**
- ✅ **Auto SSL**

### Deploy on Railway

1. Sign up: https://railway.app
2. New Project → Deploy from GitHub
3. Select your repository
4. Add environment variables
5. Deploy!

**Free tier:** $5 credit/month (usually enough for 1 small app)

---

## 🆓 Alternative: Fly.io (Free Tier)

### Why Fly.io?
- ✅ **Free tier available**
- ✅ **Global edge deployment**
- ✅ **Docker-based**

### Deploy on Fly.io

1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Sign up: `fly auth signup`
3. Create app: `fly launch`
4. Deploy: `fly deploy`

**Free tier:** 3 shared-cpu-1x VMs free, 3GB persistent storage

---

## 💰 Cost Comparison

| Platform | Free Tier | After Free Tier | Best For |
|----------|-----------|-----------------|----------|
| **AWS EC2** | ✅ 750 hrs/mo (12 months) | ~$7-10/mo | Learning AWS |
| **Render** | ✅ 750 hrs/mo (forever) | Free | Easiest, zero config |
| **Railway** | ✅ $5 credit/mo | Pay-as-you-go | Modern, easy |
| **Fly.io** | ✅ 3 VMs free | Pay-as-you-go | Global edge |

---

## 🎯 My Recommendation

### For Learning AWS:
**Use AWS EC2 Free Tier** → Follow the detailed steps above
- Learn AWS fundamentals
- Understand Linux/SSH
- Free for first year

### For Easiest Setup:
**Use Render.com** → Just connect GitHub and deploy
- Zero configuration
- Free forever
- Auto-deploy from Git

---

## 📋 Quick Setup Checklist

### AWS EC2 (Free Tier)
- [ ] AWS account created
- [ ] EC2 t2.micro instance launched
- [ ] Elastic IP allocated
- [ ] Security groups configured
- [ ] Connected via SSH
- [ ] Deployment script run
- [ ] Environment variables set
- [ ] Firebase config uploaded
- [ ] Application started
- [ ] App accessible at http://YOUR_IP

### Render.com (Free Forever)
- [ ] Render account created
- [ ] GitHub connected
- [ ] New Web Service created
- [ ] Environment variables added
- [ ] Firebase config handled
- [ ] Service deployed
- [ ] App accessible at https://your-app.onrender.com

---

## 🔒 Security Notes for Free Tier

1. **Limit SSH access** to your IP only
2. **Use strong passwords** (especially admin)
3. **Keep secrets in environment variables**
4. **Don't commit `.env` or `firebase_config.json`**
5. **Regularly update system packages**

---

## 🆘 Troubleshooting

### Can't connect via SSH
- Check security group allows SSH from your IP
- Verify key file permissions: `chmod 400 key.pem`
- Check instance is "Running"

### Application not starting
```bash
# Check logs
sudo journalctl -u cbc-ai -f

# Check service status
sudo systemctl status cbc-ai

# Verify environment variables
cat /var/www/cbc_ai/.env
```

### Out of free tier limits?
- Monitor usage in AWS Billing Dashboard
- Set up billing alerts
- Consider Render.com for truly free option

---

## 🎉 Ready to Deploy Free?

**Choose your option:**
1. **AWS EC2** → Follow Step-by-Step guide above
2. **Render.com** → Easiest, zero config
3. **Railway/Fly.io** → Modern alternatives

**All options are FREE!** 🚀


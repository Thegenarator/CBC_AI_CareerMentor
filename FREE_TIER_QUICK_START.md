# ⚡ Free Tier Quick Start

Get your app deployed for FREE in 10 minutes!

---

## 🎯 Option 1: Render.com (Easiest - 5 minutes)

### Steps:

1. **Go to Render.com** → Sign up with GitHub (FREE)

2. **New Web Service** → Connect your GitHub repo:
   ```
   https://github.com/Thegenarator/CBC_AI_CareerMentor
   ```

3. **Configure:**
   - Name: `cbch-careermentor`
   - Environment: `Python 3`
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn application:app --bind 0.0.0.0:$PORT`
   - Plan: **Free**

4. **Add Environment Variables:**
   - Copy all from your `.env` file
   - Add them one by one in Render dashboard

5. **For Firebase Config:**
   - Go to Shell in Render dashboard
   - Run: `nano firebase_config.json`
   - Paste your Firebase JSON
   - Save

6. **Deploy** → Wait 5 minutes → **Done!** 🎉

Your app: `https://cbch-careermentor.onrender.com`

---

## 🎯 Option 2: AWS EC2 (Learn AWS - 15 minutes)

### Steps:

1. **AWS Console** → EC2 → Launch Instance
   - **AMI:** Amazon Linux 2023
   - **Type:** t2.micro (FREE TIER)
   - **Key Pair:** Create & download
   - **Security:** HTTP (80), HTTPS (443), SSH (22) from your IP

2. **Connect:**
   ```bash
   ssh -i your-key.pem ec2-user@YOUR_IP
   ```

3. **Deploy:**
   ```bash
   git clone https://github.com/Thegenarator/CBC_AI_CareerMentor.git
   cd CBC_AI_CareerMentor
   chmod +x deploy_ec2.sh
   ./deploy_ec2.sh
   ```

4. **Configure:**
   ```bash
   cd /var/www/cbc_ai
   nano .env  # Paste your environment variables
   # Upload firebase_config.json via SCP or nano
   ```

5. **Start:**
   ```bash
   sudo systemctl start cbc-ai
   ```

**Done!** Your app: `http://YOUR_EC2_IP`

---

## 🎯 Option 3: Railway.app (Modern - 5 minutes)

1. Sign up: https://railway.app
2. New Project → Deploy from GitHub
3. Select repo
4. Add environment variables
5. Deploy!

**Done!** Your app: `https://your-app.railway.app`

---

## ✅ Which to Choose?

- **Learning AWS?** → EC2 Free Tier
- **Want Easiest?** → Render.com
- **Want Modern?** → Railway.app

**All are FREE!** 🎉

---

## 📝 Environment Variables Needed

Copy all these from your `.env`:

```
FIREBASE_API_KEY
FIREBASE_AUTH_DOMAIN
FIREBASE_PROJECT_ID
FIREBASE_APP_ID
OPENAI_API_KEY
GROQ_API_KEY
SECRET_KEY
ADMIN_EMAIL
ADMIN_PASSWORD
MPESA_CONSUMER_KEY
MPESA_CONSUMER_SECRET
MPESA_BUSINESS_SHORTCODE
MPESA_PASSKEY
MPESA_CALLBACK_URL
MPESA_ENVIRONMENT
FLASK_ENV=production
```

**Plus:** `firebase_config.json` file

---

## 🚀 Ready?

Pick an option above and follow the steps! You'll have a live app in minutes! 🎉


# 🚀 Render.com Deployment - Step by Step

## Why Render?
- ✅ **FREE forever** (750 hours/month)
- ✅ **No credit card needed**
- ✅ **Auto-deploy from GitHub**
- ✅ **Free SSL certificate**
- ✅ **5 minute setup**

---

## 📋 Prerequisites

- GitHub account
- Your code pushed to GitHub
- All API keys ready

---

## 🎯 Step 1: Push to GitHub

Make sure your code is on GitHub:
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

---

## 🎯 Step 2: Sign Up on Render

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with GitHub (easiest)

---

## 🎯 Step 3: Create Web Service

1. **Dashboard** → Click "New +" → "Web Service"

2. **Connect Repository:**
   - Select "Public Repository" or connect your GitHub
   - Find: `CBC_AI_CareerMentor`
   - Click "Connect"

3. **Configure Service:**
   ```
   Name: cbch-careermentor
   Region: Choose closest (Singapore, Frankfurt, etc.)
   Branch: main
   Root Directory: (leave empty)
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: python -m gunicorn application:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
   Instance Type: Free
   ```
   
   **IMPORTANT:** Use `python -m gunicorn` instead of just `gunicorn` to avoid PATH issues!

4. **Click "Create Web Service"**

---

## 🎯 Step 4: Add Environment Variables

In your service dashboard, go to **Environment** tab:

Click "Add Environment Variable" for each:

```
FIREBASE_API_KEY = your_firebase_api_key
FIREBASE_AUTH_DOMAIN = your_project.firebaseapp.com
FIREBASE_PROJECT_ID = your_project_id
FIREBASE_APP_ID = your_app_id
OPENAI_API_KEY = your_openai_key
GROQ_API_KEY = your_groq_key
SECRET_KEY = your_secret_key_here
ADMIN_EMAIL = admin@careermentor.com
ADMIN_PASSWORD = your_admin_password
MPESA_CONSUMER_KEY = your_mpesa_key
MPESA_CONSUMER_SECRET = your_mpesa_secret
MPESA_BUSINESS_SHORTCODE = your_shortcode
MPESA_PASSKEY = your_passkey
MPESA_CALLBACK_URL = https://cbch-careermentor.onrender.com/mpesa/callback
MPESA_ENVIRONMENT = sandbox
FLASK_ENV = production
```

---

## 🎯 Step 5: Upload Firebase Config

**Option A: Via Shell (Recommended)**

1. Go to your service → **Shell** tab
2. Run:
   ```bash
   nano firebase_config.json
   ```
3. Paste your Firebase service account JSON
4. Save: Ctrl+X, Y, Enter

**Option B: Via Environment Variable**

1. In Environment tab, add:
   ```
   FIREBASE_CONFIG = {"type":"service_account",...}
   ```
2. Update `app.py` to read from env if not file exists:
   ```python
   import json
   firebase_config_env = os.getenv('FIREBASE_CONFIG')
   if firebase_config_env:
       with open("firebase_config.json", "w") as f:
           json.dump(json.loads(firebase_config_env), f)
   ```

---

## 🎯 Step 6: Deploy

Render automatically deploys when you:
- Push to GitHub (auto-deploy)
- Or click "Manual Deploy"

**Wait 3-5 minutes** for build to complete.

---

## 🎯 Step 7: Access Your App

Your app will be at:
```
https://cbch-careermentor.onrender.com
```

(Or whatever you named it)

---

## ✅ Verification Checklist

- [ ] Service shows "Live" status
- [ ] Can access homepage
- [ ] Login works
- [ ] Firebase connection works
- [ ] AI features work
- [ ] Admin panel accessible

---

## 🔧 Troubleshooting

### Build Failed
- Check logs in Render dashboard
- Verify `requirements.txt` is correct
- Check Python version compatibility

### Application Crashes
- Check "Logs" tab for errors
- Verify all environment variables are set
- Check Firebase config is uploaded

### Can't Connect to Firebase
- Verify `firebase_config.json` exists
- Check Firebase environment variables
- Verify Firestore rules allow your app

### Slow Response
- Free tier has "spinner" instances (sleep after inactivity)
- First request after sleep may be slow
- Consider upgrading to paid tier for production

---

## 🔄 Auto-Deploy Setup

Render automatically deploys when you push to GitHub:

1. Make changes locally
2. Commit: `git commit -m "Update"`
3. Push: `git push origin main`
4. Render auto-deploys in ~2 minutes

---

## 🎉 Done!

Your app is now live for FREE! 🚀

**Next Steps:**
- Set up custom domain (optional)
- Monitor usage
- Scale if needed

---

## 📊 Render Free Tier Limits

- ✅ 750 hours/month (enough for 24/7)
- ✅ Free SSL
- ✅ Auto-deploy
- ⚠️ Spinner instances (sleep after 15 min inactivity)
- ⚠️ 512MB RAM
- ⚠️ 0.1 CPU

**Perfect for small apps and learning!**


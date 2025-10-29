# ✅ Pre-Deployment Checklist

Use this checklist before deploying to AWS to ensure everything is ready.

## 📦 Application Files

- [ ] `application.py` exists (WSGI entry point)
- [ ] `app.py` is configured for production
- [ ] `requirements.txt` includes all dependencies
- [ ] `Procfile` exists (for Elastic Beanstalk)
- [ ] `.ebextensions/` directory with config files
- [ ] `firebase_config.json` is ready (don't commit to git!)

## 🔑 API Keys & Configuration

- [ ] Firebase API Key - `FIREBASE_API_KEY`
- [ ] Firebase Auth Domain - `FIREBASE_AUTH_DOMAIN`
- [ ] Firebase Project ID - `FIREBASE_PROJECT_ID`
- [ ] Firebase App ID - `FIREBASE_APP_ID`
- [ ] Firebase Service Account JSON - `firebase_config.json`
- [ ] OpenAI API Key - `OPENAI_API_KEY`
- [ ] Groq API Key - `GROQ_API_KEY`
- [ ] Flask Secret Key - `SECRET_KEY` (strong, random)
- [ ] Admin Email - `ADMIN_EMAIL`
- [ ] Admin Password - `ADMIN_PASSWORD` (strong password)
- [ ] M-Pesa Consumer Key - `MPESA_CONSUMER_KEY`
- [ ] M-Pesa Consumer Secret - `MPESA_CONSUMER_SECRET`
- [ ] M-Pesa Business Shortcode - `MPESA_BUSINESS_SHORTCODE`
- [ ] M-Pesa Passkey - `MPESA_PASSKEY`
- [ ] M-Pesa Callback URL - `MPESA_CALLBACK_URL` (must be HTTPS)
- [ ] M-Pesa Environment - `MPESA_ENVIRONMENT` (sandbox/production)

## 🔒 Security

- [ ] All API keys are in `.env` file (not in code)
- [ ] `.env` is in `.gitignore`
- [ ] `firebase_config.json` is in `.gitignore`
- [ ] No hardcoded credentials in code
- [ ] Admin password is strong
- [ ] Secret key is random and secure
- [ ] HTTPS/SSL configured (for production)

## 🌐 AWS Setup

- [ ] AWS Account created
- [ ] AWS CLI installed
- [ ] EB CLI installed (`eb --version`)
- [ ] AWS credentials configured
- [ ] Region selected
- [ ] Security groups configured (if using EC2)

## 📝 Code Quality

- [ ] Application runs locally without errors
- [ ] All dependencies installed successfully
- [ ] No debug mode enabled in production
- [ ] Error handling implemented
- [ ] Logging configured

## 🧪 Testing

- [ ] Application starts successfully locally
- [ ] All routes work correctly
- [ ] Firebase connection works
- [ ] API integrations work
- [ ] Static files load correctly

## 📊 Monitoring

- [ ] CloudWatch logging set up (EB automatically)
- [ ] Error tracking configured (optional)
- [ ] Backup strategy planned

## 🚀 Deployment

- [ ] Environment variables documented
- [ ] Deployment guide reviewed
- [ ] Rollback plan ready
- [ ] Team notified (if applicable)

## After Deployment

- [ ] Application accessible via URL
- [ ] All pages load correctly
- [ ] Authentication works
- [ ] Firebase connection works
- [ ] API calls succeed
- [ ] M-Pesa callbacks work (test)
- [ ] Admin panel accessible
- [ ] Static files load correctly
- [ ] HTTPS redirects work (if configured)
- [ ] Performance acceptable

---

## 🆘 Emergency Contacts

- AWS Support: https://console.aws.amazon.com/support
- Documentation: `AWS_DEPLOYMENT_GUIDE.md`

---

**Save this checklist and use it for every deployment!**


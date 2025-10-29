# M-Pesa Integration - Configuration Guide

## ✅ Your M-Pesa Credentials Are Configured!

Your M-Pesa API credentials have been successfully integrated into the system:

### **Consumer Key**: 
`GnMdAhLo9w1oGUApZpWh9myVB0G35tTqchfkKAdhtmifCeoK`

### **Consumer Secret**: 
`Pr1n6TFKcMqj7iYkVfA7HnvQAnUeYO2MBcx8SbGScVyQAGDXOSADiInJ7gGdxtpD`

### **Business Shortcode**: 
`174379` (Sandbox)

### **Environment**: 
`Sandbox` (for testing)

---

## 📋 Additional Configuration Needed

To complete the M-Pesa integration, you need to add these to your `.env` file:

### **1. M-Pesa Passkey**
Get this from your Safaricom Developer Portal:
- Log in to https://developer.safaricom.co.ke/
- Go to your application
- Copy the Passkey

Add to `.env`:
```env
MPESA_PASSKEY=your_passkey_from_portal
```

### **2. Callback URL**
This must be a publicly accessible HTTPS URL where M-Pesa will send payment confirmations.

For local testing, you can use:
- **ngrok**: `ngrok http 5000` (get the HTTPS URL)
- **localtunnel**: `lt --port 5000` (get the HTTPS URL)

Add to `.env`:
```env
MPESA_CALLBACK_URL=https://your-ngrok-url.ngrok.io/mpesa/callback
```

### **3. Complete .env File**
Create a `.env` file in your project root with:

```env
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Groq API Key
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile

# Flask Secret Key
SECRET_KEY=your_secret_key_change_this_in_production

# Admin Credentials
ADMIN_EMAIL=admin@careermentor.com
ADMIN_PASSWORD=admin123

# M-Pesa Configuration
MPESA_CONSUMER_KEY=GnMdAhLo9w1oGUApZpWh9myVB0G35tTqchfkKAdhtmifCeoK
MPESA_CONSUMER_SECRET=Pr1n6TFKcMqj7iYkVfA7HnvQAnUeYO2MBcx8SbGScVyQAGDXOSADiInJ7gGdxtpD
MPESA_BUSINESS_SHORTCODE=174379
MPESA_PASSKEY=your_passkey_here
MPESA_CALLBACK_URL=https://your-domain.com/mpesa/callback
MPESA_ENVIRONMENT=sandbox
```

---

## 🧪 Testing M-Pesa Integration

### **1. Test Phone Numbers**
Use these test numbers in sandbox:
- `254708374149` - Test phone number
- Any amount (no real money deducted)

### **2. Test Payment Flow**
1. Start your Flask app: `python app.py`
2. Open dashboard and click "Subscribe to Premium"
3. Select a plan
4. Enter test phone number: `254708374149`
5. Click "Pay with M-Pesa"
6. Check your phone for M-Pesa prompt
7. Enter PIN: `0000` (test PIN)
8. Payment should be processed

### **3. Verify Integration**
Check the console for:
- ✅ "Access token retrieved successfully"
- ✅ "STK Push initiated successfully"
- ✅ "Payment callback received"

---

## 🚀 Going to Production

When ready for live payments:

1. **Apply for Production Access**
   - Submit application in Safaricom Developer Portal
   - Provide business registration documents
   - Wait for approval (1-2 weeks)

2. **Update Credentials**
   - Get production Consumer Key & Secret
   - Get production Business Shortcode
   - Get production Passkey

3. **Update .env**
   ```env
   MPESA_ENVIRONMENT=production
   MPESA_CONSUMER_KEY=production_consumer_key
   MPESA_CONSUMER_SECRET=production_consumer_secret
   MPESA_BUSINESS_SHORTCODE=your_production_shortcode
   MPESA_PASSKEY=your_production_passkey
   ```

4. **Set Up SSL**
   - Ensure your domain has valid SSL certificate
   - Update callback URL to production domain

---

## 📊 Subscription Plans

Your platform includes three subscription tiers:

| Plan | Price | Features |
|------|-------|----------|
| **Basic** | KSh 300/month | 20 AI interactions, Basic CV, 1 premium feature |
| **Premium** | KSh 500/month | Unlimited AI, All features, Priority support |
| **Professional** | KSh 1,000/month | Everything + Team management + API access |

---

## 🔒 Security Notes

1. **Never commit `.env` file** to version control
2. **Keep credentials secure** - Don't share publicly
3. **Use HTTPS** for all production endpoints
4. **Validate callbacks** - Always verify payment confirmations
5. **Monitor transactions** - Log all payment attempts

---

## ✅ Current Status

- ✅ M-Pesa credentials integrated
- ✅ Payment API endpoints created
- ✅ Subscription management system ready
- ✅ User interface components implemented
- ⏳ Waiting for Passkey configuration
- ⏳ Waiting for Callback URL setup

---

## 🎯 Next Steps

1. **Get Passkey** from Safaricom Developer Portal
2. **Set up Callback URL** using ngrok or similar
3. **Test payment flow** with sandbox credentials
4. **Apply for production** when ready
5. **Launch** with real payments

Your M-Pesa integration is ready to go! 🚀💰


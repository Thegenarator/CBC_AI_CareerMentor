# 🔧 Fix: Gunicorn Command Not Found on Render

## Problem
You're seeing this error:
```
bash: line 1: gunicorn: command not found
==> Exited with status 127
```

## Solution Options

### ✅ Solution 1: Use Python Module (Recommended)

Change your **Start Command** in Render to:

```
python -m gunicorn application:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

This uses Python's module system to find gunicorn, which is more reliable.

---

### ✅ Solution 2: Fix Build Command

Make sure your **Build Command** is:
```
pip install --upgrade pip && pip install -r requirements.txt
```

This ensures pip is updated and all packages are installed.

---

### ✅ Solution 3: Use Full Path (Alternative)

If the above doesn't work, try:
```
~/.local/bin/gunicorn application:app --bind 0.0.0.0:$PORT
```

---

## 🎯 Complete Render Configuration (Fixed)

Here's the correct configuration for Render:

### Build Command:
```
pip install --upgrade pip && pip install -r requirements.txt
```

### Start Command:
```
python -m gunicorn application:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

### Other Settings:
- **Runtime:** Python 3
- **Root Directory:** (leave empty)
- **Branch:** main

---

## 📝 Step-by-Step Fix

1. **Go to Render Dashboard** → Your Service → Settings

2. **Update Build Command:**
   - Scroll to "Build Command"
   - Change to: `pip install --upgrade pip && pip install -r requirements.txt`
   - Click "Save Changes"

3. **Update Start Command:**
   - Scroll to "Start Command"
   - Change to: `python -m gunicorn application:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
   - Click "Save Changes"

4. **Redeploy:**
   - Go to "Manual Deploy" or push to GitHub
   - Wait for deployment

---

## ✅ Verify requirements.txt

Make sure your `requirements.txt` includes gunicorn:

```txt
Flask==3.0.0
openai>=1.0.0
firebase-admin>=6.0.0
python-dotenv>=1.0.0
fpdf>=2.5.0
httpx>=0.24.0
requests>=2.31.0
cryptography>=41.0.0
gunicorn>=21.2.0
flask-cors>=4.0.0
```

---

## 🔍 Debug Steps

If still not working:

1. **Check Build Logs:**
   - Render Dashboard → Logs
   - Verify `pip install -r requirements.txt` succeeded
   - Look for any errors

2. **Check if gunicorn installed:**
   - Go to Shell tab
   - Run: `python -m pip list | grep gunicorn`
   - Should show: `gunicorn 21.2.0` (or similar)

3. **Test gunicorn manually:**
   - In Shell: `python -m gunicorn --version`
   - Should show version number

---

## 🚀 Quick Fix (Copy-Paste Ready)

**Build Command:**
```
pip install --upgrade pip && pip install -r requirements.txt
```

**Start Command:**
```
python -m gunicorn application:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

**That's it!** Save and redeploy. 🎉


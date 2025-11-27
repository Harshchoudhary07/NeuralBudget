# 🌐 Free Hosting Deployment Guide - Render.com

This guide will help you deploy your NeuralBudget application to **Render.com** for **FREE**.

## Why Render.com?
- ✅ **Free tier** with 750 hours/month
- ✅ **Automatic deployments** from GitHub
- ✅ **Free PostgreSQL database**
- ✅ **Easy environment variable management**
- ✅ **HTTPS included**

---

## Prerequisites
- ✅ Project uploaded to GitHub (see [GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md))
- ✅ Gemini API Key: `AIzaSyD-2oOFUFTRmfPL7Yx354sb_zJzPVuJrTs`
- ⚠️ Firebase service account key (firebase_key.json) - **You'll need to get this**

---

## Step 1: Create a Render Account

1. Go to [Render.com](https://render.com)
2. Click **"Get Started"**
3. Sign up using your **GitHub account** (recommended)
4. Verify your email address

---

## Step 2: Create a New Web Service

1. From your Render dashboard, click **"New +"**
2. Select **"Web Service"**
3. Click **"Connect a repository"**
4. If prompted, authorize Render to access your GitHub repositories
5. Find and select your **NeuralBudget** repository
6. Click **"Connect"**

---

## Step 3: Configure Your Web Service

Fill in the following details:

### Basic Settings:
- **Name**: `neuralbudget` (or any name you prefer)
- **Region**: Choose the closest region to you
- **Branch**: `main`
- **Root Directory**: Leave blank
- **Runtime**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn neural_budget.wsgi:application`

### Instance Type:
- Select **"Free"** plan

---

## Step 4: Set Environment Variables

Scroll down to **"Environment Variables"** section and add the following:

Click **"Add Environment Variable"** for each:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Generate a random key [here](https://djecrety.ir/) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.render.com` |
| `GEMINI_API_KEY` | `AIzaSyD-2oOFUFTRmfPL7Yx354sb_zJzPVuJrTs` |
| `FIREBASE_API_KEY` | Your Firebase API Key (get from Firebase Console) |
| `ENVIRONMENT` | `production` |
| `PYTHON_VERSION` | `3.10.0` |

### Optional Email Settings (for password reset):
| Key | Value |
|-----|-------|
| `EMAIL_BACKEND` | `django.core.mail.backends.smtp.EmailBackend` |
| `EMAIL_HOST` | `smtp.gmail.com` (or your email provider) |
| `EMAIL_PORT` | `587` |
| `EMAIL_USE_TLS` | `True` |
| `EMAIL_HOST_USER` | Your email address |
| `EMAIL_HOST_PASSWORD` | Your email app password |
| `DEFAULT_FROM_EMAIL` | Your email address |

---

## Step 5: Add PostgreSQL Database (Optional but Recommended)

1. Go back to your Render dashboard
2. Click **"New +"** → **"PostgreSQL"**
3. Fill in:
   - **Name**: `neuralbudget-db`
   - **Database**: `neuralbudget`
   - **User**: `neuralbudget_user`
   - **Region**: Same as your web service
   - **Plan**: **Free**
4. Click **"Create Database"**
5. Once created, copy the **"Internal Database URL"**
6. Go back to your **Web Service** → **Environment** tab
7. Add environment variable:
   - **Key**: `DATABASE_URL`
   - **Value**: Paste the Internal Database URL

---

## Step 6: Handle Firebase Credentials

Since `firebase_key.json` cannot be uploaded to GitHub, you have two options:

### Option A: Use Environment Variable (Recommended)
1. Open your `firebase_key.json` file
2. Copy the entire JSON content
3. In Render, add environment variable:
   - **Key**: `FIREBASE_CREDENTIALS`
   - **Value**: Paste the entire JSON content

4. Update your Django settings to read from environment variable (I can help with this)

### Option B: Manual Upload via Render Shell
1. After deployment, go to your web service
2. Click **"Shell"** tab
3. Upload the file manually using the file upload feature

---

## Step 7: Deploy!

1. Scroll to the bottom
2. Click **"Create Web Service"**
3. Render will start building and deploying your application
4. This may take 5-10 minutes

### Monitor Deployment:
- Watch the **"Logs"** tab to see the build progress
- Look for any errors in red

---

## Step 8: Verify Deployment

Once deployment is complete:

1. Render will provide a URL like: `https://neuralbudget.onrender.com`
2. Click the URL to open your application
3. Test the following:
   - ✅ Home page loads
   - ✅ Login page loads
   - ✅ Signup page loads
   - ✅ Static files (CSS/JS) are working

---

## 🎉 Success!

Your NeuralBudget application is now live and accessible to anyone with the URL!

**Your App URL**: `https://your-app-name.onrender.com`

---

## 📝 Important Notes

### Free Tier Limitations:
- ⚠️ **Spins down after 15 minutes of inactivity**
- ⚠️ **First request after inactivity may take 30-60 seconds** (cold start)
- ⚠️ **750 hours/month** (enough for one app running 24/7)

### Firebase Firestore:
- The app uses Firebase Firestore for data storage
- Make sure your Firebase project is set up correctly
- Firestore is free for small usage

---

## 🔧 Updating Your App

Whenever you push changes to GitHub:

```powershell
git add .
git commit -m "Your update message"
git push
```

Render will **automatically** rebuild and redeploy your app!

---

## 🐛 Troubleshooting

### Issue: Build Failed
**Solution**: 
- Check the **Logs** tab for error messages
- Common issues:
  - Missing dependencies in `requirement.txt`
  - Syntax errors in code
  - Missing environment variables

### Issue: App shows "Application Error"
**Solution**:
- Check **Logs** tab for runtime errors
- Verify all environment variables are set correctly
- Make sure `ALLOWED_HOSTS` includes `.render.com`

### Issue: Static files not loading
**Solution**:
- Make sure `build.sh` runs `collectstatic`
- Check that `STATIC_ROOT` is set in `settings.py`
- Verify WhiteNoise is installed and configured

### Issue: Database errors
**Solution**:
- Make sure migrations ran successfully (check logs)
- Verify `DATABASE_URL` is set correctly
- Try running migrations manually via Render Shell

### Issue: Firebase errors
**Solution**:
- Verify `FIREBASE_CREDENTIALS` environment variable is set
- Check that Firebase project is active
- Ensure Firestore is enabled in Firebase Console

---

## 🆘 Need Help?

1. Check Render's [documentation](https://render.com/docs)
2. Check the **Logs** tab for detailed error messages
3. Review Django's deployment [checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)

---

## 🔐 Security Reminders

- ✅ Never commit `.env` or `firebase_key.json` to GitHub
- ✅ Use strong, random `SECRET_KEY`
- ✅ Keep `DEBUG = False` in production
- ✅ Regularly update dependencies for security patches

# 🚀 Quick Start Guide - NeuralBudget

Welcome! This guide will help you get your NeuralBudget application from your local machine to the internet in just a few steps.

## 📋 What You Have
- ✅ NeuralBudget project downloaded from GitHub
- ✅ Gemini API Key: `AIzaSyD-2oOFUFTRmfPL7Yx354sb_zJzPVuJrTs`

## 📋 What You Need
- [ ] GitHub account ([Sign up free](https://github.com/join))
- [ ] Render.com account ([Sign up free](https://render.com))
- [ ] Firebase service account key (optional for full functionality)

---

## 🎯 Two Simple Steps

### Step 1: Upload to GitHub (15 minutes)
Follow the detailed guide: **[GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md)**

**Quick Summary:**
1. Create a new repository on GitHub
2. Open PowerShell in your project folder
3. Run these commands:
   ```powershell
   cd C:\Users\harsh\Downloads\NeuralBudget-main\NeuralBudget-main
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/NeuralBudget.git
   git push -u origin main
   ```

### Step 2: Deploy to Render.com (20 minutes)
Follow the detailed guide: **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)**

**Quick Summary:**
1. Sign up on Render.com with your GitHub account
2. Create a new Web Service
3. Connect your GitHub repository
4. Add environment variables (especially `GEMINI_API_KEY`)
5. Click "Create Web Service"
6. Wait 5-10 minutes for deployment

---

## 🎉 That's It!

Your app will be live at: `https://your-app-name.onrender.com`

---

## 📚 Detailed Guides

- **[GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md)** - Complete GitHub upload instructions
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Complete Render.com deployment instructions
- **[README.md](README.md)** - Project documentation and features

---

## ⚡ Important Notes

### Free Tier Limitations:
- Your app will "sleep" after 15 minutes of inactivity
- First visit after sleep takes 30-60 seconds to wake up
- This is normal for free hosting!

### Security:
- ✅ Never share your API keys publicly
- ✅ The `.gitignore` file protects your sensitive files
- ✅ Always use environment variables for secrets

---

## 🆘 Need Help?

1. Check the detailed guides mentioned above
2. Look at the troubleshooting sections in each guide
3. Check Render's logs tab for error messages

---

## 🎊 Congratulations!

You're about to have your own AI-powered finance manager live on the internet!

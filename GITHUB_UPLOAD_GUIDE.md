# 🚀 GitHub Upload Guide for NeuralBudget

This guide will help you upload your NeuralBudget project to GitHub.

## Prerequisites
- Git installed on your computer ([Download Git](https://git-scm.com/downloads))
- A GitHub account ([Create one here](https://github.com/join))

---

## Step 1: Create a New GitHub Repository

1. Go to [GitHub](https://github.com) and log in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `NeuralBudget` (or any name you prefer)
   - **Description**: "AI-Powered Personal Finance Management System"
   - **Visibility**: Choose **Public** or **Private**
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

---

## Step 2: Initialize Git in Your Project

Open **PowerShell** or **Command Prompt** and navigate to your project directory:

```powershell
cd C:\Users\harsh\Downloads\NeuralBudget-main\NeuralBudget-main
```

Initialize Git (if not already initialized):

```powershell
git init
```

---

## Step 3: Configure Git (First Time Only)

If this is your first time using Git, configure your name and email:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Step 4: Add Files to Git

Add all files to Git (this respects .gitignore, so sensitive files won't be added):

```powershell
git add .
```

Check what files will be committed:

```powershell
git status
```

> ✅ **Verify**: Make sure `.env` and `firebase_key.json` are NOT listed in green (they should be ignored)

---

## Step 5: Create Your First Commit

```powershell
git commit -m "Initial commit: NeuralBudget AI Finance Manager"
```

---

## Step 6: Connect to GitHub Repository

Replace `YOUR_USERNAME` with your actual GitHub username:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/NeuralBudget.git
```

---

## Step 7: Push to GitHub

Push your code to GitHub:

```powershell
git branch -M main
git push -u origin main
```

> 💡 **Note**: You may be prompted to log in to GitHub. Use your GitHub username and password (or personal access token if 2FA is enabled).

---

## Step 8: Verify Upload

1. Go to your GitHub repository in your browser
2. Refresh the page
3. You should see all your project files

### ✅ Security Check:
- **Verify** that `.env` file is **NOT** visible on GitHub
- **Verify** that `firebase_key.json` is **NOT** visible on GitHub
- **Verify** that `db.sqlite3` is **NOT** visible on GitHub

---

## 🎉 Success!

Your project is now on GitHub! You can share the repository URL with others or proceed to deployment.

**Next Step**: Follow the [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) to deploy your application to Render.com for free hosting.

---

## 📝 Common Issues

### Issue: "fatal: remote origin already exists"
**Solution**: Remove the existing remote and add it again:
```powershell
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/NeuralBudget.git
```

### Issue: Authentication failed
**Solution**: 
- If you have 2FA enabled, you need to create a [Personal Access Token](https://github.com/settings/tokens)
- Use the token as your password when pushing

### Issue: Files are being rejected
**Solution**: Make sure your `.gitignore` file is properly configured and you've run `git add .` again.

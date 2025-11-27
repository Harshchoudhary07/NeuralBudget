# 🐍 PythonAnywhere Deployment Guide

This guide will help you deploy **NeuralBudget** to **PythonAnywhere** for free.

## ✅ Prerequisites
1.  **Sign up** for a free account at [PythonAnywhere.com](https://www.pythonanywhere.com/).
2.  **Verify your email** (important!).
3.  Have your GitHub URL ready: `https://github.com/Harshchoudhary07/NeuralBudget`

---

## 🚀 Step 1: Open the Console

1.  Log in to your PythonAnywhere dashboard.
2.  Click on the **"Consoles"** tab.
3.  Click on **"Bash"** to open a terminal.

---

## 📥 Step 2: Clone Your Code

In the Bash console, run these commands (copy-paste them one by one):

```bash
# 1. Clone your repository
git clone https://github.com/Harshchoudhary07/NeuralBudget.git

# 2. Go into the project folder
cd NeuralBudget
```

---

## 🛠️ Step 3: Set Up Virtual Environment

Create a virtual environment to install your dependencies:

```bash
# 1. Create virtual environment (this takes a minute)
mkvirtualenv --python=/usr/bin/python3.10 myenv

# 2. Install dependencies (this takes a few minutes)
pip install -r requirement.txt
```

> **Note:** If you see any errors about `langchain` versions, don't worry, we fixed them in the repo!

---

## 🔑 Step 4: Configure Environment Variables

You need to create a `.env` file on PythonAnywhere.

1.  In the Bash console, run:
    ```bash
    nano .env
    ```
2.  **Copy** the content from your local `.env.example` file (or see below).
3.  **Paste** it into the console (Right-click > Paste).
4.  **Fill in your real keys** (Secret Key, Gemini Key, Firebase Credentials).

**Template to copy:**
```ini
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=.pythonanywhere.com
GEMINI_API_KEY=AIzaSyD-2oOFUFTRmfPL7Yx354sb_zJzPVuJrTs
ENVIRONMENT=production
# Add your Firebase credentials here as a single line JSON if needed
# FIREBASE_CREDENTIALS=...
```

5.  Save and exit:
    - Press `Ctrl + X`
    - Press `Y`
    - Press `Enter`

---

## 🗄️ Step 5: Database & Static Files

Run these commands to set up the database and static files:

```bash
# 1. Run database migrations
python manage.py migrate

# 2. Collect static files (Type 'yes' if asked)
python manage.py collectstatic
```

---

## 🌐 Step 6: Configure Web App

1.  Go to the **"Web"** tab (top right).
2.  Click **"Add a new web app"**.
3.  Click **"Next"**.
4.  Select **"Manual configuration"** (NOT Django).
5.  Select **"Python 3.10"**.
6.  Click **"Next"**.

### 🔧 Configure Settings (Scroll down on Web tab):

**1. Virtualenv:**
- Enter path: `/home/yourusername/.virtualenvs/myenv`
- (Replace `yourusername` with your actual PythonAnywhere username)
- Click the **Check mark** ✅ to save.

**2. Code:**
- Source code: `/home/yourusername/NeuralBudget`
- Working directory: `/home/yourusername/NeuralBudget`

**3. WSGI Configuration File:**
- Click the link that looks like `/var/www/yourusername_pythonanywhere_com_wsgi.py`.
- **Delete everything** in that file.
- **Paste** this code:

```python
import os
import sys

# 1. Add your project folder to sys.path
path = '/home/yourusername/NeuralBudget'
if path not in sys.path:
    sys.path.append(path)

# 2. Load .env file
from dotenv import load_dotenv
project_folder = os.path.expanduser(path)
load_dotenv(os.path.join(project_folder, '.env'))

# 3. Set Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'neural_budget.settings'

# 4. Activate Django app
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
- **IMPORTANT:** Replace `yourusername` with your actual username in the `path` variable!
- Click **"Save"** (top right) and go back to the Web tab.

**4. Static Files:**
- Under **"Static files"** section:
- Click **"Enter URL"**: `/static/`
- Click **"Enter path"**: `/home/yourusername/NeuralBudget/staticfiles`
- Click **Check mark** ✅.

---

## 🚀 Step 7: Launch!

1.  Scroll to the top of the **Web** tab.
2.  Click the big green **"Reload"** button.
3.  Click the link at the top (e.g., `yourusername.pythonanywhere.com`).

**Your app should be live!** 🎉

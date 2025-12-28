# 🛠️ Developer Setup Guide — Unsaid (Windows)

**Follow only your section below.**  
All commands are for **Windows** (Command Prompt / PowerShell).

---

## 🔑 COMMON RULES (READ ONCE)

- ✅ Clone the repo **only once**
- ✅ Work **only on your assigned branch**
- ❌ Do **not** push to `main`
- ✅ Commit **only your screen-related files**

---

## ✅ THE CORRECT ORDER 
```
Clone / Pull → Checkout branch → Create & activate venv → Install deps → Run app
```

**This is the cleanest and safest flow**, especially when branches or requirements may change.

---

## 🔹 STEP 1: CLONE THE REPOSITORY (ONE TIME ONLY)
```cmd
git clone https://github.com/lalith-thexplorer/unsaid-ai.git
cd unsaid-ai
```

---

## 🔹 STEP 2: CHECK OUT YOUR ASSIGNED BRANCH (FIRST)

**Do this before creating the virtual environment.**

### 👤 Lalith — Chat Screen
```cmd
git checkout screen/chat
```

### 👤 Sri Vidya — Crisis / Safety Overlay
```cmd
git checkout screen/safety
```

### 👤 Nikhil — Mood Insights + Export
```cmd
git checkout screen/insights-export
```

### 👤 Ruthvika — Landing / Onboarding
```cmd
git checkout screen/onboarding
```

### 👤 Rohith — Mood Badge Check-In
```cmd
git checkout screen/mood-checkin
```

📌 **Why this step is here:** So everyone starts from the correct branch state, not `main`.

---

## 🔹 STEP 3: CREATE VIRTUAL ENVIRONMENT (ONE TIME)
```cmd
python -m venv venv
```

---

## 🔹 STEP 4: ACTIVATE VIRTUAL ENVIRONMENT (EVERY TIME)
```cmd
venv\Scripts\activate
```

✅ You must see `(venv)` in the terminal.

---

## 🔹 STEP 5: INSTALL DEPENDENCIES
```cmd
pip install -r requirements.txt
```

📌 If `requirements.txt` changes later, re-run this step.

---

## 🔹 STEP 6: RUN THE APP
```cmd
streamlit run app.py
```

The app will open in your browser.

---

## 🔄 DAILY WORKFLOW (EVERY DAY)

### Before starting work:
```cmd
git pull origin main
```
⚠️ If there are conflicts, **stop and ask**.

### After making changes:
```cmd
git add .
git commit -m "Update <screen-name>"
git push origin <your-branch-name>
```

**Example:**
```cmd
git push origin screen/chat
```

---

## 🚫 COMMON MISTAKES THIS ORDER PREVENTS

- ❌ Installing packages on the wrong branch
- ❌ Running outdated code from `main`
- ❌ Conflicting virtual environments
- ❌ "It works on my system" issues

---

## ✅ QUICK SELF-CHECK (MANDATORY)

Run these and confirm:

### 1️⃣ Check your branch:
```cmd
git branch
```
✔️ Your branch has `*`

### 2️⃣ Verify Python is from venv:
```cmd
where python
```
✔️ Points to `venv\Scripts\python.exe`

### 3️⃣ Launch the app:
```cmd
streamlit run app.py
```
✔️ App launches

**If all three pass → you're set.** 🎉

---

## 📞 Need Help?

If you encounter issues, reach out in the whatsapp group with:
- Your branch name
- The error message
- What step you were on

---

**Happy coding! 🚀**


# Screen Flow — Unsaid

This document describes the **user navigation flow** of the Unsaid application.
It is intended to help developers understand **screen order, transitions, and conditional paths**.

---

## 🔁 Primary User Flow

1. **Landing / Onboarding Screen**  
   - App introduction  
   - Non-medical disclaimer  
   - Optional trusted contact input  
   - Entry point into the app  

   ↓

2. **Mood Badge Check-In Screen**  
   - User selects one or more mood badges  
   - Option to skip  
   - Selected moods are passed forward  

   ↓

3. **Chat Screen (Core Experience)**  
   - AI opens conversation referencing selected moods  
   - User types freely  
   - AI listens empathetically  
   - Optional coping suggestions may appear  

---

## ⚠️ Conditional Flow — Safety Support

- **Crisis / Safety Overlay Screen**
  - Triggered only if high-risk or harmful language is detected
  - Overlays on top of the Chat Screen
  - Displays:
    - Concern message
    - Helpline numbers
    - Option to notify trusted contact (if provided)
  - User may:
    - Continue chatting
    - Exit the app

---

## 📊 Optional Reflection Flow

From the **Chat Screen**, the user may choose to:

4. **Mood Insight Screen (Heat Map)**  
   - Visual reflection of recent mood check-ins  
   - Short-term data only  
   - No diagnosis or scoring  

   ↓

5. **Reflection Summary / Export Screen**  
   - Preview of reflection summary  
   - Option to download PDF or HTML  
   - Non-medical disclaimer included  

---

## 🔚 Exit & Continuation

From any screen, the user may:
- Continue chatting
- Start a new mood check-in
- Close the app

---

## 🧠 Flow Summary (One Line)

**Onboarding → Mood Check-In → Chat → (Safety if needed) → Insights → Export → End**

---

## 📌 Notes

- No login is required at any stage  
- All emotional data is stored locally on the user’s device  
- Safety actions are transparent and user-controlled  
- No medical advice or diagnosis is provided  

---

This flow is **intentionally simple** to support clarity, ethics, and demo reliability.

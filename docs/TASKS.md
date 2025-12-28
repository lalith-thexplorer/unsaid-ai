# ✅ TASK CHECKLISTS — UNSAID

### 🌐 Global Requirement (For ALL screens)
* **Theme:** Dark theme
* **UI Style:** Modern glassmorphism
* **Vibe:** Calm, minimal, premium look
* **Constraints:** No bright colors, no clutter

---

## 🧠 Lalith — Chat Screen (Core Experience)
**Branch:** `screen/chat`  
**File:** `screens/chat.py`

### ✅ Checklist
- [ ] Create chat layout (AI + user messages)
- [ ] Dark glass-style chat bubbles
- [ ] Text input box with send button
- [ ] Auto-scroll to latest message
- [ ] Display AI response clearly
- [ ] Reference selected mood badges in AI replies
- [ ] Handle empty input gracefully
- [ ] Add placeholder for coping card below chat
- [ ] Ensure smooth UX (spacing, readability)
- [ ] No medical language or diagnosis

> **📌 Done when:** User can chat smoothly and feel “heard”.

---

## 🧠 Sri Vidya — Crisis / Safety Overlay Screen
**Branch:** `screen/safety`  
**File:** `screens/safety.py`

### ✅ Checklist
- [ ] Create full-screen overlay UI (glass style)
- [ ] Show calm concern message (not alarming)
- [ ] Display helpline numbers clearly
- [ ] Add “Notify trusted contact” button (if exists)
- [ ] Add “Continue chatting” option
- [ ] Ensure overlay appears only on trigger
- [ ] Add non-medical disclaimer visibly
- [ ] No automatic actions without user consent
- [ ] Dark theme, supportive colors only

> **📌 Done when:** Crisis flow feels ethical, transparent, and calm.

---

## 🧠 Nikhil — Mood Insights + Export Screens
**Branch:** `screen/insights-export`  
**Files:** `screens/insights.py`, `screens/export.py`

### ✅ Checklist (Insights Screen)
- [ ] Create “View Insights” navigation
- [ ] Render mood heat map using Plotly
- [ ] Dark-theme chart styling
- [ ] Show recent sessions only
- [ ] Add “Clear my data” option
- [ ] Add “This is not a diagnosis” note
- [ ] Glass card container for chart

### ✅ Checklist (Export Screen)
- [ ] Create reflection summary preview
- [ ] Include dates + moods + notes
- [ ] Add “Download PDF / HTML” button
- [ ] Ensure disclaimer appears in export
- [ ] Clean formatting (readable, simple)

> **📌 Done when:** Insights look polished and export works end-to-end.

---

## 🎨 Ruthvika — Landing / Onboarding Screen
**Branch:** `screen/onboarding`  
**File:** `screens/onboarding.py`

### ✅ Checklist
- [ ] Display app name: **Unsaid**
- [ ] Show tagline clearly
- [ ] Short non-medical disclaimer
- [ ] Optional trusted contact input field
- [ ] “Start” button
- [ ] Dark gradient background
- [ ] Glass-style main card
- [ ] Calm, welcoming UI
- [ ] No clutter or long text

> **📌 Done when:** First impression feels safe and premium.

---

## 🎨 Rohith — Mood Badge Check-In Screen
**Branch:** `screen/mood-checkin`  
**File:** `screens/mood_checkin.py`

### ✅ Checklist
- [ ] Show prompt: “How are you feeling right now?”
- [ ] Display 6–8 emoji mood badges
- [ ] Support multi-select
- [ ] Clear selected / unselected states
- [ ] Glass-style badge buttons
- [ ] Continue button
- [ ] Skip option
- [ ] Pass selected moods forward
- [ ] Smooth hover / click interaction
- [ ] Dark theme consistency

> **📌 Done when:** Mood selection feels effortless and intuitive.

---

## 📌 GENERAL RULES (APPLY TO ALL)
* ❌ **No new features** beyond checklist
* ❌ **No pushing directly** to `main`
* ✅ **Commit frequently** to your branch
* ✅ **UI quality** > feature quantity
* ✅ **Ask** before touching shared files

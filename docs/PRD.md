# Product Requirements Document (PRD)

## Product Name
**Unsaid**

**Tagline:**  
*A space for what you can’t say out loud.*

---

## 1. Product Overview

### 1.1 Purpose
Unsaid is a **privacy-first, non-medical AI emotional support web application** designed to help users express emotions they struggle to articulate. It provides empathetic listening, gentle coping support, and ethical safety guidance — **without requiring accounts, tracking users, or offering medical advice**.

Unsaid does **not** diagnose, treat, or replace professional mental health care.

---

### 1.2 Problem Statement
Many people experience emotional distress but hesitate to seek help due to:
- Fear of judgment  
- Difficulty expressing emotions  
- Stigma around mental health  
- Privacy concerns with existing apps  

Most existing solutions:
- Feel clinical or diagnostic  
- Require logins and long questionnaires  
- Push advice too early  
- Store sensitive emotional data  

---

### 1.3 Solution Summary
Unsaid lowers the barrier to emotional expression by:
- Letting users start with simple **mood badges**
- Offering **empathetic AI listening**
- Providing **optional, micro-level coping actions**
- Handling crisis situations **ethically and transparently**
- Keeping all emotional data **local and user-controlled**

---

## 2. Goals & Non-Goals

### 2.1 Product Goals
- Help users express emotions safely and easily  
- Feel human, calm, and non-judgmental  
- Respect privacy by default  
- Be fully demo-ready in a **4-day hackathon**

---

### 2.2 Non-Goals (Explicitly Out of Scope)
Unsaid will **not**:
- Provide medical advice or diagnosis  
- Require user login or authentication  
- Track users across devices  
- Store emotional data on servers  
- Offer therapy matching or user-to-user chat  
- Send push notifications  
- Automatically contact emergency services  

---

## 3. Target Users & Personas

### 🎓 The Overwhelmed Student
Needs a quick, judgment-free place to vent during exams or deadlines.

### 🧭 The Therapy-Seeker
Considering professional help but struggles to put feelings into words.

### 🔐 The Privacy-Conscious User
Avoids mental health apps due to fear of data misuse.

---

## 4. Core User Experience Flow (High Level)

1. User opens Unsaid  
2. Sees mood badge check-in  
3. Selects one or more emotions  
4. Enters AI chat  
5. AI listens and responds empathetically  
6. Optional coping suggestion appears  
7. Crisis support appears if needed  
8. User views short-term mood insights  
9. User exports a reflection summary  

---

## 5. Functional Requirements

### FR1: Mood Badge Check-In (Entry Point)
**Description:**  
Users express how they feel using emoji-based badges.

**Requirements:**
- Prompt: *“How are you feeling right now?”*
- 6–8 emoji mood badges
- Multi-select support
- “Continue” button
- Option to skip

**Data Captured:**
- Selected moods
- Timestamp

**Constraints:**
- No scoring  
- No labeling  
- No forced choice  

---

### FR2: Active Listening Chat Engine
**Description:**  
AI chat interface focused on reflection, not fixing.

**Requirements:**
- Text-based chat UI
- AI must:
  - Reference selected moods
  - Validate emotions
  - Use calm, human language
  - Avoid diagnosis or medical terminology

**Example:**
> “I see you’re feeling anxious and tired. That sounds heavy. Want to tell me what’s been going on?”

---

### FR3: Emotion-Aware Response Logic
**Description:**  
AI adapts responses based on emotional context.

**Emotional States:**
- Venting (listening only)
- Seeking relief (gentle support)
- Distressed (grounding)
- Crisis (safety response)

**Adjustments:**
- Tone
- Length
- Coping card visibility

---

### FR4: Guided Coping Cards
**Description:**  
Optional, contextual coping suggestions.

**Requirements:**
- One card at a time
- Dismissible
- Examples:
  - 60-second breathing exercise
  - Grounding prompt
  - One-line journaling

**Constraints:**
- No therapy jargon
- No forced participation
- No external browsing

---

### FR5: Transparent Safety Nudge (Crisis Support)
**Description:**  
Ethical handling of crisis or self-harm language.

**Triggers:**
- Crisis keywords
- High-risk emotional patterns

**Behavior:**
- Clear safety overlay
- Encourage reaching out for help
- Display local helplines
- Optional **opt-in safety net**:
  - Trusted contact chosen during onboarding
  - Alerts sent **only with consent**
  - No silent actions

**Constraints:**
- No automatic emergency calls
- No third-party alerts without opt-in
- Non-medical disclaimer always visible

---

### FR6: Short-Term Mood Insight (Heat Map)
**Description:**  
Visual reflection of recent emotional check-ins.

**Requirements:**
- Heat map or simple chart
- Covers recent sessions only
- No scores or interpretation

**Data Handling:**
- Stored locally on device
- Never sent to server
- User can clear anytime

---

### FR7: Shareable Reflection Summary (Insight Bridge)
**Description:**  
Exportable summary to support professional conversations.

**Requirements:**
- Includes:
  - Dates
  - Selected moods
  - User notes
- Format:
  - PDF or HTML
- Disclaimer included:
  > “This is not a medical assessment.”

---

### FR8: Non-Medical Disclaimer
**Placement:**
- Onboarding
- Crisis overlay
- Exported summary

**Message:**
> “Unsaid provides emotional support only and does not offer medical advice or diagnosis.”

---

## 6. Technical Stack

- **Platform:** Web Application  
- **Framework:** Streamlit (Python)  
- **AI Engine:** Gemini 1.5 Flash API  
- **Visualization:** Plotly  
- **Export:** FPDF / HTML  
- **Storage:** Local session state  
- **Safety Logic:** Rule-based detection  

---

## 7. Privacy & Ethics Requirements
- No login or accounts
- No PII collected
- No server-side emotional data storage
- User-controlled visibility
- Transparent crisis handling
- No medical claims

---

## 8. Success Criteria (Hackathon Context)
- Smooth live demo
- Judges understand value within 2 minutes
- No privacy or ethics red flags
- Clear differentiation from generic chatbots

---

## 9. Final Product Statement
**Unsaid** is a privacy-first, non-medical AI companion that helps people express what they can’t say out loud — by listening with empathy, offering gentle support, and guiding them safely toward real-world help.

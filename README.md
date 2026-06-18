# 🌿 AI Health Companion

**AI Health Companion** is a Streamlit web app powered by Google Gemini 2.5 Flash that acts as your personal nutrition and health advisor. It lets you save a health profile (goals, conditions, dietary preferences), then uses that context to generate personalised 7-day meal plans, analyse food photos for calorie and macro breakdowns, and answer health & nutrition questions with science-backed guidance — all in one clean, tabbed interface.

---

## 🧭 Overview

**AI Health Companion** is an intelligent, conversational health and nutrition assistant built with Streamlit and Google's Gemini 2.5 Flash model. It empowers users to make informed dietary decisions through three core capabilities: AI-generated personalised meal plans, real-time food image analysis, and science-backed answers to health questions — all tailored to a user-defined health profile.

---

## ✨ Features

### 🥗 Personalised Meal Planning
- Generates a complete **7-day meal plan** (breakfast, lunch, dinner & snacks)
- Accounts for health goals, medical conditions, fitness routines, food preferences, and dietary restrictions
- Provides a **daily nutritional breakdown** (calories and macronutrients)
- Includes a **categorised shopping list** and preparation tips
- Supports one-click **download** of the full meal plan as a `.txt` file

### 📸 Food Image Analysis
- Upload any food photo (JPG / PNG) for instant AI analysis
- Returns **estimated calories**, macronutrient breakdown (protein, carbs, fat, fibre), and key micronutrients
- Highlights potential **health benefits** and dietary concerns
- Provides **suggested portion sizes** and analyses multi-item meals individually

### 💡 Health & Nutrition Insights
- Ask any health or nutrition question in plain language
- Responses are **science-backed**, contextual, and personalised to the saved health profile
- Includes practical recommendations, precautions, and relevant study references
- Suggests foods or supplements where appropriate

### 👤 Health Profile Sidebar
- Persistent **session-state health profile** covering goals, conditions, routines, preferences, and restrictions
- Visual **profile snapshot chips** for a quick status overview
- Profile updates are applied instantly across all tabs

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Frontend / UI** | [Streamlit](https://streamlit.io/) |
| **AI Model** | [Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) |
| **AI SDK** | `google-generativeai` |
| **Image Processing** | [Pillow (PIL)](https://python-pillow.org/) |
| **Environment Config** | `python-dotenv` |
| **Language** | Python 3.9+ |

---

## 📖 Usage Guide

1. **Set up your Health Profile** — Fill in the sidebar fields (goals, conditions, routines, preferences, restrictions) and click **Save Profile**.

2. **Meal Planning tab** — Add any specific requirements (e.g., *"quick weeknight meals"*) and click **Generate Meal Plan**. Download the result when done.

3. **Food Analysis tab** — Upload a photo of your meal and click **Analyse Food** to receive a full nutritional breakdown.

4. **Health Insights tab** — Type a health or nutrition question and click **Get Insights** for a personalised, evidence-informed response.

---

## ⚠️ Disclaimer

AI Health Companion is intended **for informational and educational purposes only**. The AI-generated content does not constitute medical advice. Always consult a qualified healthcare professional or registered dietitian before making changes to your diet, exercise routine, or health management plan.

---

## Author

**Snehit Sabale**
[GitHub](https://github.com/snehitsabale2108)

---
<div align="center">
  Made with 🌿 using Streamlit & Google Gemini
</div>

# 🍬 Treat Tracker: AI-Powered Hide & Seek

A "Vibe Coded" personal assistant that helps me remember where I hide ttreats. This project uses an **iOS Shortcut** to dictate voice notes, a **FastAPI** backend to extract intent using **Google Gemini**, and saves the results directly to **Apple Notes**.

[Image of a system architecture diagram showing iPhone voice dictation, a FastAPI backend, and an Apple Notes integration]

---

## 🚀 How It Works

1. **Capture**: Long-press your iPhone's Action Button or tap a Home Screen widget and say: *"I hid the Oreos behind the cookbooks in the kitchen."*
2. **Process**: The iOS Shortcut sends that text to this **FastAPI** backend hosted on **Replit**.
3. **Analyze**: The backend uses **Google Gemini 1.5 Flash** to parse the messy sentence into a structured JSON object:
   ```json
   {
     "treat": "Oreos",
     "location": "Kitchen - behind the cookbooks",
     "date": "2026-03-22"
   }

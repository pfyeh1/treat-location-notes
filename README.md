# Treat Tracker API

A lightweight, serverless Python API that uses Apple iOS Shortcuts and Google Gemini AI to log and track hidden objects (like treats) in real-time. Project integrates iOS shortcuts, backend logic, and NLP processing (Gemini) to turn turn unstructured voice or text inputs into structured data logs in iOS notes.

---

## Architecture Overview

1. **Client (iOS Shortcut):** Captures user voice/text input (e.g., *"I hid the Kinder Joy in the laundry room"*). Sends a secure `POST` request with the raw text payload to the backend API.
2. **Backend API (FastAPI):** Receives the request, validates the schema using Pydantic models, and forwards the unstructured string to the Gemini API.
3. **AI Layer (Google Gemini):** Parses the string to extract the `treat` and `location` as explicit, structured data fields.
4. **Storage (Apple Notes):** The Shortcut receives the structured data back from the API and cleanly appends a formatted, timestamped log entry directly into a designated Apple Note.

---

## Repository Structure

```text
├── main.py              # Application logic (FastAPI endpoints & Gemini configuration)
├── requirements.txt     # Python production dependencies
├── Dockerfile           # OCI-compliant container instructions for cloud deployment
├── .dockerignore        # Excludes local/build noise from cloud images
└── README.md            # System documentation

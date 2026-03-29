# Treat Parser API

## Overview

A FastAPI (Python) app that uses Google Gemini AI to extract a treat and its location from free-form text.

## Stack

- **Language**: Python 3.11
- **API framework**: FastAPI + uvicorn (hot reload enabled)
- **AI**: Google Gemini (`google-genai`) via Replit AI Integrations — no API key required
- **Validation**: Pydantic

## Project Structure

```
main.py            # FastAPI app — all routes and Gemini logic
requirements.txt   # Python dependencies
pyproject.toml     # Python project metadata (managed by uv)
uv.lock            # Locked dependency versions
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/healthz` | Health check |
| POST | `/api/parse-treat` | Extract treat + location from text |

### Example

```bash
curl -X POST http://localhost/api/parse-treat \
  -H "Content-Type: application/json" \
  -d '{"text": "I hid the Oreos behind the flour"}'

# → {"treat": "Oreos", "location": "behind the flour"}
```

## Running

Click the green **Run** button — it starts `python main.py` which launches uvicorn on `PORT` (default 8000) with hot reload.

## Environment Variables

Set automatically by Replit — do not modify:
- `AI_INTEGRATIONS_GEMINI_API_KEY`
- `AI_INTEGRATIONS_GEMINI_BASE_URL`

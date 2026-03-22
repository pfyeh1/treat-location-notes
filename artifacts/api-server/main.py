import os
import json
import re
from google import genai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

gemini_api_key = os.environ.get("AI_INTEGRATIONS_GEMINI_API_KEY")
gemini_base_url = os.environ.get("AI_INTEGRATIONS_GEMINI_BASE_URL")

if not gemini_api_key:
    raise RuntimeError("AI_INTEGRATIONS_GEMINI_API_KEY must be set.")
if not gemini_base_url:
    raise RuntimeError("AI_INTEGRATIONS_GEMINI_BASE_URL must be set.")

client = genai.Client(
    api_key=gemini_api_key,
    http_options={"base_url": gemini_base_url, "api_version": ""},
)

app = FastAPI(root_path="/api")


class ParseTreatRequest(BaseModel):
    text: str


class ParseTreatResponse(BaseModel):
    treat: str
    location: str


@app.get("/healthz")
async def health():
    return {"status": "ok"}


@app.post("/parse-treat", response_model=ParseTreatResponse)
async def parse_treat(body: ParseTreatRequest):
    prompt = (
        'You are a text parser. Extract the treat and its location from the following text.\n'
        'Respond ONLY with a JSON object in this exact format: {"treat": "<treat name>", "location": "<location>"}\n'
        'Do not include any explanation, markdown, or extra text.\n\n'
        f'Text: "{body.text}"'
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    raw = response.text or ""
    match = re.search(r'\{[\s\S]*\}', raw)
    if not match:
        raise HTTPException(status_code=500, detail="Failed to parse response from AI")

    try:
        data = json.loads(match.group())
        return ParseTreatResponse(**data)
    except Exception:
        raise HTTPException(status_code=500, detail="AI response did not match expected schema")

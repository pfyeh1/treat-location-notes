import { Router, type IRouter } from "express";
import { ai } from "@workspace/integrations-gemini-ai";
import { ParseTreatBody, ParseTreatResponse } from "@workspace/api-zod";

const router: IRouter = Router();

router.post("/parse-treat", async (req, res) => {
  const parsed = ParseTreatBody.safeParse(req.body);
  if (!parsed.success) {
    res.status(400).json({ error: "Invalid request body", details: parsed.error.errors });
    return;
  }

  const { text } = parsed.data;

  const prompt = `You are a text parser. Extract the treat and its location from the following text.
Respond ONLY with a JSON object in this exact format: {"treat": "<treat name>", "location": "<location>"}
Do not include any explanation, markdown, or extra text.

Text: "${text}"`;

  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: [{ role: "user", parts: [{ text: prompt }] }],
    config: { maxOutputTokens: 8192 },
  });

  const raw = response.text ?? "";
  const jsonMatch = raw.match(/\{[\s\S]*\}/);
  if (!jsonMatch) {
    req.log.error({ raw }, "Gemini did not return valid JSON");
    res.status(500).json({ error: "Failed to parse response from AI" });
    return;
  }

  const result = ParseTreatResponse.safeParse(JSON.parse(jsonMatch[0]));
  if (!result.success) {
    req.log.error({ raw }, "AI response did not match expected schema");
    res.status(500).json({ error: "AI response did not match expected schema" });
    return;
  }

  res.json(result.data);
});

export default router;

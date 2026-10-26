# AI Email Assistant

A small API starter for generating structured email drafts from a user's intent. It separates request validation from the generation provider so an LLM can be added without coupling the API to a specific vendor.

## Capabilities
- Accept recipient context, goal, tone, and key points.
- Return a deterministic template draft in the baseline implementation.
- Keep sending email separate from drafting; no email is sent automatically.

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Visit `/docs` to try the endpoint.

## Responsible design
- Treat email content and retrieved context as untrusted input.
- Never expose API keys in source control; load them from environment variables.
- Ask for user approval before sending.
- Avoid inventing facts, commitments, dates, or attachments.
- Add provider timeouts, retry limits, rate limiting, and audit logging for a real deployment.

## Next steps
Implement an LLM adapter behind `DraftProvider`, add prompt-injection tests, redact sensitive logs, and evaluate output quality across job, academic, and business email scenarios.

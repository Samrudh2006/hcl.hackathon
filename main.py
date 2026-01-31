from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

API_KEY = "mySecretHoneypotKey2006"

@app.post("/honeypot")
async def honeypot(request: Request):
    key = request.headers.get("x-api-key")

    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    data = await request.json()

    return {
        "scam_detected": True,
        "agent_active": True,
        "response": "Okay sir, I am confused. Can you please explain what I need to do?",
        "extracted_intelligence": {
            "upi_ids": [],
            "bank_accounts": [],
            "phishing_urls": []
        }
    }

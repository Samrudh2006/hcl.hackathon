from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

API_KEY = "mySecretHoneypotKey2006"

# Accept both /honeypot and /honeypot/ to avoid 405 errors
@app.api_route("/honeypot", methods=["POST"])
@app.api_route("/honeypot/", methods=["POST"])
async def honeypot(request: Request):
    # Check API key in headers
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Ensure JSON body
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON body")

    # Example response (you can enhance your intelligence extraction later)
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

# Optional: root endpoint to quickly test server is running
@app.get("/")
async def root():
    return {"status": "FastAPI honeypot API is running"}

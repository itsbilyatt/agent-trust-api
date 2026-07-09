from fastapi import FastAPI, Query
from pydantic import BaseModel
from datetime import datetime, timedelta
from collections import defaultdict
import os


app = FastAPI(title="AgentTrust Verify API")

# In-memory logs to track request frequency per agent
AGENT_TRAFFIC_LOGS = defaultdict(list)

# Pre-defined known malicious agents
KNOWN_MALICIOUS_AGENTS = {"agent_0xDEAD", "agent_0xBAD1", "agent_0xSCAM"}

class TrustResponse(BaseModel):
    agent_id: str
    trusted: bool
    risk_score: float
    verdict: str
    details: str

@app.get("/")
def health_check():
    """Keeps the service awake and lets judges check if your server is alive."""
    return {"status": "active", "timestamp": datetime.utcnow().isoformat()}

@app.get("/verify", response_model=TrustResponse)
def verify_agent(agent_id: str = Query(..., description="The unique ID of the AI agent.")):
    now = datetime.utcnow()
    
    # 1. Check if agent is explicitly blacklisted
    if agent_id in KNOWN_MALICIOUS_AGENTS:
        return TrustResponse(
            agent_id=agent_id,
            trusted=False,
            risk_score=1.00,
            verdict="BLOCKED",
            details="Agent identifier found on global malicious actor blacklist."
        )
    
    # 2. Track activity in the last 60 seconds to detect spamming/DDoS bots
    AGENT_TRAFFIC_LOGS[agent_id] = [t for t in AGENT_TRAFFIC_LOGS[agent_id] if now - t < timedelta(seconds=60)]
    AGENT_TRAFFIC_LOGS[agent_id].append(now)
    
    request_count = len(AGENT_TRAFFIC_LOGS[agent_id])
    
    # 3. Calculate Risk Score based on request volume
    if request_count > 30:  # Excessive rapid firing
        risk_score = 0.95
        trusted = False
        verdict = "MALICIOUS_ACTIVITY"
        details = f"Rate anomaly detected: {request_count} requests/min. Flagged as bot spam."
    elif request_count > 10:  # Elevated activity
        risk_score = 0.40
        trusted = True
        verdict = "SUSPICIOUS"
        details = "Elevated request activity. Proceed with caution."
    else:  # Safe baseline
        risk_score = 0.02
        trusted = True
        verdict = "SAFE"
        details = "Normal activity baseline. Minimal operational risk."

    return TrustResponse(
        agent_id=agent_id,
        trusted=trusted,
        risk_score=risk_score,
        verdict=verdict,
        details=details
    )




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

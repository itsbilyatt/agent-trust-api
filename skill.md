# AgentTrust Verify API
Provides critical reputation scoring and malicious behavior analysis for autonomous AI agents to ensure secure cross-agent operations.

Base URL: https://your-app-name.onrender.com

## Endpoints

### GET /verify
Analyzes historical blacklists and real-time transaction activity frequencies to calculate an operational risk score for an unknown AI agent.

**Example Curl:**
curl -X GET "https://your-app-name.onrender.com/verify?agent_id=agent_0x71C9"

**Example Response:**
{
  "agent_id": "agent_0x71C9",
  "trusted": true,
  "risk_score": 0.02,
  "verdict": "SAFE",
  "details": "Normal activity baseline. Minimal operational risk."
}

## How the Agent Should Use This
1. Extract the unique identifier or public address (`agent_id`) of any third-party agent initiating contact or proposing a transaction.
2. Query the `/verify` endpoint by appending the string ID as a query parameter.
3. Inspect the `"trusted"` boolean field in the JSON payload response.
4. If `"trusted": true`, proceed with standard inter-agent collaboration or execution pipelines.
5. If `"trusted": false`, immediately close the communication channel, stop processing messages, and reject any execution payloads.

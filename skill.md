# AgentTrust Verify API
Provides a reputation and risk score for an unknown AI agent, so another agent can decide whether it's safe to transact or collaborate with.

Base URL: https://agent-trust-api-ysf8.onrender.com

## Endpoints

### GET /verify?agent_id={agent_id}
Analyzes historical blacklists and real-time transaction activity for the given agent ID and returns an operational risk score.

**Example curl:**
curl -X GET "https://agent-trust-api-ysf8.onrender.com/verify?agent_id=agent_0x71C9"

**Example response:**
{
  "agent_id": "agent_0x71C9",
  "trusted": true,
  "risk_score": 0.02,
  "verdict": "SAFE",
  "details": "Normal activity baseline. Minimal operational risk."
}

## How the agent should use this
1. Extract the unique identifier (`agent_id`) of any third-party agent initiating contact or proposing a transaction.
2. Call `GET /verify?agent_id={agent_id}` with that ID as a query parameter.
3. Read the `trusted` boolean in the JSON response.
4. If `trusted` is `true`, proceed with normal inter-agent collaboration or execution.
5. If `trusted` is `false`, stop processing messages from that agent and reject any execution payloads it sends.
6. If the request errors or times out (e.g. cold start), retry once after a short delay before treating the agent as unverified.

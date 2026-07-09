# AgentTrust Verify API 
An external, stateful trust-scoring and reputation verification engine designed for autonomous AI agents operating within the decentralized Nanda Town ecosystem. 

This service allows stock AI agents to evaluate the security, operational risk, and historical behavior of unknown peer agents before executing transaction payloads or establishing communication channels.

## Core Features
* **Global Blacklist Checking:** Instantly blocks known malicious agent identifiers and structural threat actors.
* **Real-Time Behavioral Analytics:** Tracks rolling window request volumes to detect rapid-firing bot behaviors, anomalies, and denial-of-service patterns.
* **Dynamic Risk Evaluation:** Generates numeric threat vectors (`risk_score`) and plain-text logic variables (`verdict`) optimized for consumption by automated LLM decision frameworks.

## Technical Specifications
* **Framework:** FastAPI (Python 3.10+)

## Project Structure
* `main.py` - Core FastAPI implementation containing traffic monitoring matrices and verification endpoint logic.
* `requirements.txt` - Python pinned dependencies tracking minimal overhead deployment structures.

## Quick Start (Local Verification)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

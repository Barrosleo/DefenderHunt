#!/usr/bin/env python3
"""
Simulate a basic security incident for testing playbooks and scripts.
"""

import json

def simulate():
    incident = {
        "id": 1001,
        "type": "Simulated Phishing",
        "user": "jane.doe@contoso.com",
        "timestamp": "2025-10-16T12:00:00Z",
        "details": "Phishing email delivered with malicious link."
    }
    with open("simulated_incident.json", "w") as f:
        json.dump(incident, f, indent=2)
    print("Simulated incident generated: simulated_incident.json")

if __name__ == "__main__":
    simulate()

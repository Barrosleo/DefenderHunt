# DefenderHunt: Threat Hunting & Incident Response Toolkit

## 1. Project Goal & Overview

Develop a GitHub repository—**DefenderHunt**—that serves both as an **educational resource** and a **practical tool** for **SOC analysts, cloud security engineers, and cybersecurity students**. It demonstrates real-world threat hunting, incident response, and automation using Microsoft Defender tools, KQL, and MITRE ATT&CK.

## 2. Core Components & Functionality

- **Threat Hunting Playbooks**  
  Python scripts and KQL queries to hunt for suspicious activity across endpoints, identities, and cloud telemetry.  
  Tech: KQL, Microsoft Sentinel, Defender XDR

- **MITRE ATT&CK Mapper**  
  Python tool that maps IOCs to MITRE techniques and visualizes them.  
  Tech: Python, Pandas, Plotly

- **Incident Analysis Playbooks**  
  Markdown-based guides for triage, root-cause analysis, and containment strategies aligned with MITRE ATT&CK, D3FEND, and Engage.  
  Tech: Markdown, MITRE Frameworks

- **Automation & Reporting Tools**  
  Scripts to enrich alerts, generate incident reports, and streamline SOC workflows.  
  Tech: Python, Jinja2, Defender API

- **Cloud Config Checker**  
  Script to validate Azure security configurations and suggest remediations.  
  Tech: Python, Azure SDK

## 3. Getting Started & Installation

### Prerequisites
- Python 3.8+
- pip
- (Optional) Azure credentials for cloud config checks

### Installation
```bash
git clone https://github.com/Barrosleo/DefenderHunt.git
cd DefenderHunt
pip install -r requirements.txt
```

## 4. Usage Examples

- Run a Threat Hunting Query
```bash
python src/threat_hunting/hunt_runner.py --query src/threat_hunting/queries/suspicious_logon.kql
```

- Map IOCs to MITRE Techniques
```bash
from src.mitre_mapper.mitre_mapper import map_iocs
map_iocs("iocs.csv")
```

- Generate Incident Report
```bash
python src/automation/report_generator.py --incident_id 12345
```

- Enrich Alerts in Bulk
```bash
python src/automation/enrich_alerts.py --input alerts.csv --output enriched_alerts.csv
```

- Check Azure Configurations
```bash
python src/cloud_config_checker/azure_config_check.py
```

## 5. Supporting Resources & Documentation
MITRE Cheat Sheet Explains ATT&CK tactics, techniques, and procedures with real-world examples. 
```bash
docs/MITRE_CheatSheet.md
```

Incident Playbooks Markdown guides for phishing, lateral movement, and privilege escalation response. 
```bash
docs/Incident_Playbooks.md
```

## 6. Technical Considerations
Languages: Python, KQL

Libraries: pandas, plotly, jinja2, azure-identity, azure-mgmt-security

Data Sources: Defender XDR, Sentinel, CSV files

Deployment: Local machine or Azure VM

Version Control: Git/GitHub

## 7. Desired Outcomes/Impact
Improve analyst efficiency

Enhance understanding of MITRE ATT&CK and threat hunting

Provide hands-on experience with Defender tools

## 8. Contributing
We welcome contributions! See ```CONTRIBUTING.md``` for guidelines.

## 9. License
This project is licensed under the MIT License. See ```LICENSE``` for details.

## 10. Acknowledgements
MITRE ATT&CK Framework

AlienVault OTX for threat data

Microsoft Sentinel and Defender APIs

## 11. Contact
GitHub: @Barrosleo 
LinkedIn: www.linkedin.com/in/leonardo-cybersecuritypro <img width="468" height="24" alt="image" src="https://github.com/user-attachments/assets/4aa08f92-badb-4927-9653-8408d3117098" />


    
# KAIRI Anthropic Cybersecurity Skills

<div align="center">
<img width="1600" height="711" alt="mop" src="https://github.com/user-attachments/assets/47758fdd-5615-4b2e-803c-eb4370c4b7e1" />

[![X (Twitter)](https://img.shields.io/badge/X-Follow-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/KairiSkills)
![CA](https://img.shields.io/badge/CA-Coming%20Soon-00FF41?style=for-the-badge)

![KAIRI-Skills Banner](https://img.shields.io/badge/KAIRI-Skills-00FF41?style=for-the-badge&logo=terminal&logoColor=black)
![MIT License](https://img.shields.io/badge/License-MIT-00FF41?style=for-the-badge)
![Build Status](https://img.shields.io/badge/Status-Production--Ready-00FF41?style=for-the-badge)
![100 Skills](https://img.shields.io/badge/Skills-100+-00FF41?style=for-the-badge)

**Advanced Cybersecurity Skill Database for AI Agents & Security Professionals**

[Overview](#overview) • [Features](#features) • [Skill Categories](#skill-categories) • [Getting Started](#getting-started) • [Contributing](#contributing) • [License](#license)

</div>

---

## Overview

**KAIRI-Skills** is a comprehensive, open-source cybersecurity skills repository designed for AI agents and security practitioners. Each skill is structured with detailed documentation including prerequisites, workflows, code examples, and verification steps.

> "Security is not a product, but a process." — Bruce Schneier

### Why KAIRI-Skills?

- **Structured Documentation** — Every skill follows a consistent format for maximum clarity
- **Production-Ready** — Real-world tested workflows with working code examples
- **AI-Optimized** — Designed for AI agents to understand and execute security tasks
- **MIT Licensed** — Free to use, modify, and distribute

---

## Features

| Feature | Description |
|---------|-------------|
| **Structured Format** | Uniform SKILL.md format with When to Use, Prerequisites, Workflow, and Verification sections |
| **Code Examples** | Bash, Python, and YAML commands for immediate implementation |
| **Tool References** | Complete list of tools and systems required for each skill |
| **Common Scenarios** | Real-world use cases with approach and pitfalls |
| **Verification Steps** | How to validate skill execution success |
| **MITRE ATT&CK Mapping** | Threat technique coverage for detection rules |

---

## Skill Categories

Our skills are organized into three primary action categories:

### 🔍 Analyzing (70 skills)
Skills focused on analyzing cybersecurity artifacts, logs, malware, and forensic evidence.

```
analyzing-network-traffic-with-wireshark/
analyzing-memory-dumps-with-volatility/
analyzing-malware-behavior-with-cuckoo-sandbox/
analyzing-docker-container-forensics/
analyzing-windows-registry-for-artifacts/
analyzing-threat-intelligence-feeds/
...
```

### 🔧 Auditing (15 skills)
Skills focused on auditing cloud infrastructure and security configurations.

```
auditing-aws-s3-bucket-permissions/
auditing-azure-active-directory-configuration/
auditing-kubernetes-cluster-rbac/
auditing-terraform-infrastructure-for-security/
auditing-cloud-with-cis-benchmarks/
...
```

### ⚙️ Building (15 skills)
Skills focused on building security infrastructure, pipelines, and automation.

```
building-detection-rules-with-sigma/
building-incident-response-dashboard/
building-ioc-enrichment-pipeline-with-opencti/
building-c2-infrastructure-with-sliver-framework/
building-devsecops-pipeline-with-gitlab-ci/
...
```

---

## Skill Structure

Each skill follows a consistent, AI-readable format:

```markdown
# Skill Name

## When to Use
- Scenario 1
- Scenario 2

## Prerequisites
- Tool 1
- Tool 2

## Workflow
### Step 1: Description
Code examples and detailed instructions

### Step 2: Description
Code examples and detailed instructions

## Verification
How to verify successful execution

## Tools & Systems
- Tool 1
- Tool 2

## Common Scenarios
### Scenario: Description
Approach and pitfalls
```

### Example Skill File

```
skills/
├── analyzing-network-traffic-with-wireshark/
│   └── SKILL.md          # Complete skill documentation
├── auditing-aws-s3-bucket-permissions/
│   └── SKILL.md
└── building-detection-rules-with-sigma/
    └── SKILL.md
```

---

## Getting Started

### Quick Start

```bash
# Clone the repository
git clone https://github.com/Axxxxxxaaann/KAIRI-Skills.git

# Navigate to the project
cd KAIRI-Skills

# List available skills
ls skills/

# Read a skill
cat skills/analyzing-network-traffic-with-wireshark/SKILL.md
```

### Prerequisites

Depending on the skill, you may need:

- **Linux/Unix Environment** (Linux, macOS, WSL2)
- **Python 3.8+** with required packages
- **Cloud CLI Tools** (AWS CLI, Azure CLI, GCP SDK)
- **Security Tools** (Wireshark, Volatility, Burp Suite, etc.)
- **API Access** for threat intelligence services

---

## Featured Skills

### Network Security

| Skill | Description | Level |
|-------|-------------|-------|
| [Analyzing Network Traffic with Wireshark](skills/analyzing-network-traffic-with-wireshark/) | Packet capture analysis for intrusion detection | Advanced |
| [Analyzing Network Packets with Scapy](skills/analyzing-network-packets-with-scapy/) | Craft custom packets for security testing | Advanced |
| [Analyzing DNS Logs for Exfiltration](skills/analyzing-dns-logs-for-exfiltration/) | Detect DNS tunneling and data exfiltration | Advanced |

### Cloud Security

| Skill | Description | Level |
|-------|-------------|-------|
| [Auditing AWS S3 Bucket Permissions](skills/auditing-aws-s3-bucket-permissions/) | Identify publicly exposed S3 data | Intermediate |
| [Auditing Kubernetes Cluster RBAC](skills/auditing-kubernetes-cluster-rbac/) | Review K8s role-based access controls | Advanced |
| [Analyzing Kubernetes Audit Logs](skills/analyzing-kubernetes-audit-logs/) | Monitor K8s security events | Advanced |

### Digital Forensics & Incident Response

| Skill | Description | Level |
|-------|-------------|-------|
| [Analyzing Memory Dumps with Volatility](skills/analyzing-memory-dumps-with-volatility/) | Memory forensics for malware detection | Advanced |
| [Analyzing Windows Event Logs with Splunk](skills/analyzing-windows-event-logs-in-splunk/) | SIEM-based forensic analysis | Intermediate |
| [Analyzing PowerShell Script Block Logging](skills/analyzing-powershell-script-block-logging/) | Detect PowerShell-based attacks | Advanced |

### Malware Analysis

| Skill | Description | Level |
|-------|-------------|-------|
| [Analyzing Malicious PDF with peepdf](skills/analyzing-malicious-pdf-with-peepdf/) | PDF malware analysis techniques | Intermediate |
| [Analyzing Macro Malware in Office Documents](skills/analyzing-macro-malware-in-office-documents/) | Office document malware detection | Intermediate |
| [Analyzing Packed Malware with UPX](skills/analyzing-packed-malware-with-upx-unpacker/) | Unpack and analyze compressed malware | Advanced |

---

## Tool Coverage

Our skills cover a comprehensive range of security tools:

### Network Security
- Wireshark, tcpdump, tshark, Scapy, NetFlow, Zeek

### Cloud Security
- AWS CLI, Azure CLI, Prowler, ScoutSuite, IAM Access Analyzer

### Memory & Forensics
- Volatility 2/3, WinPmem, LiME, Autopsy, FTK

### Malware Analysis
- Ghidra, IDA Pro, peepdf, pefile, YARA, Cuckoo Sandbox

### SIEM & Detection
- Splunk, Elastic Security, Sigma, MITRE ATT&CK Navigator

### Container Security
- Docker, Kubernetes, Trivy, kube-bench, Dive

---

## Contributing

Contributions are welcome! Please read our guidelines:

1. **Fork the Repository** — Create your own copy
2. **Add Skills** — Follow the SKILL.md format
3. **Test Workflows** — Ensure code examples work
4. **Submit PR** — Include detailed descriptions

### Skill Contribution Template

```markdown
# New Skill Name

## When to Use
Describe when this skill should be used.

## Prerequisites
List required tools and access.

## Workflow
### Step 1: [Title]
Code and detailed instructions

## Verification
How to verify success.

## Tools & Systems
- Tool 1
- Tool 2
```

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 KAIRI-Skills

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## Related Projects

- [MITRE ATT&CK](https://attack.mitre.org/) — Framework for threat techniques
- [Sigma](https://github.com/SigmaHQ/sigma) — Detection rule format
- [OWASP](https://owasp.org/) — Web application security resources

---

## Connect

<p align="center">
<a href="https://github.com/Axxxxxxaaann/KAIRI-Skills"><img src="https://img.shields.io/badge/GitHub-100+-00FF41?style=social&logo=github" alt="GitHub"></a>
<a href="https://github.com/Axxxxxxaaann"><img src="https://img.shields.io/badge/Author-Axxxxxxaaann-00FF41?style=social" alt="Author"></a>
</p>

---

<div align="center">

**Made with 🔐 for the security community**

*Built for AI agents & security practitioners*

</div>

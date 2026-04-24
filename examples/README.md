# KAIRI-Skills Examples

Welcome to the examples directory! Here you'll find real-world examples of how to use the skills in this repository.

## Quick Start Examples

### 1. Network Traffic Analysis

Using Wireshark for packet analysis:

```bash
# Capture network traffic
sudo tshark -i eth0 -c 100 -w capture.pcap

# Analyze the capture
wireshark capture.pcap
```

**Skill**: `analyzing-network-traffic-with-wireshark`

---

### 2. Building Detection Rules

Creating Sigma rules for SIEM:

```yaml
title: Suspicious PowerShell Download
status: experimental
author: KAIRI Community
logsource:
  product: windows
  service: powershell
detection:
  selection:
    EventID: 4104
    ScriptBlockText|contains:
      - 'Invoke-WebRequest'
      - 'DownloadFile'
  condition: selection
level: high
```

**Skill**: `building-detection-rules-with-sigma`

---

### 3. Cloud Security Audit

Auditing AWS S3 bucket permissions:

```bash
#!/bin/bash
# List all S3 buckets
aws s3 ls

# Check bucket ACLs
aws s3api get-bucket-acl --bucket my-bucket

# Check public access settings
aws s3api get-public-access-block --bucket my-bucket
```

**Skill**: `auditing-aws-s3-bucket-permissions`

---

## Workflow Examples

### Incident Response Workflow

```
1. Detection & Analysis
   └── Use: analyzing-network-traffic-with-wireshark
   └── Use: analyzing-windows-event-logs

2. Containment
   └── Use: isolating-affected-systems
   └── Use: blocking-malicious-ips

3. Eradication
   └── Use: removing-malware-artifacts
   └── Use: patching-vulnerabilities

4. Recovery
   └── Use: restoring-from-backups
   └── Use: verifying-system-integrity
```

### Malware Analysis Workflow

```
1. Static Analysis
   └── Use: static-malware-analysis-with-peframe
   └── Use: analyzing-android-malware-with-apktool

2. Dynamic Analysis
   └── Use: dynamic-malware-analysis-in-sandbox
   └── Use: analyzing-memory-with-volatility

3. Reporting
   └── Use: generating-malware-analysis-report
```

---

## Integration Examples

### CI/CD Integration

```yaml
# .github/workflows/security-scan.yml
name: Security Skills Scan

on: [push, pull_request]

jobs:
  sigma-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Sigma rules
        run: |
          git clone https://github.com/SigmaHQ/sigma.git
          sigma convert -r rules/ -o /tmp/alerts
```

### SIEM Integration

```python
# siem_integration.py
from sigma.rule import SigmaRule

def process_sigma_rule(rule_path):
    """Process a Sigma rule and send to SIEM"""
    rule = SigmaRule.from_yaml(rule_path)
    alerts = rule.detect()
    send_to_siem(alerts)
```

---

## Community Contributions

These examples are contributions from the community. See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to add your own examples!

### Example Categories

- **Network Analysis**: Wireshark, tcpdump, Zeek
- **Cloud Security**: AWS, Azure, GCP auditing
- **Malware Analysis**: Static and dynamic analysis
- **Threat Hunting**: MITRE ATT&CK, detection rules
- **Forensics**: Disk, memory, and log forensics

---

## Resources

- [Official Documentation](https://github.com/Axxxxxxaaann/KAIRI-Skills)
- [Sigma Rules Repository](https://github.com/SigmaHQ/sigma)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

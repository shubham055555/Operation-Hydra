# Operation Hydra - Tools, Commands & Justification

## 1. PowerShell

Purpose:
Project creation, file generation and evidence inspection.

Commands Used:
- tree /F
- Get-ChildItem
- Get-Content
- Set-Content

Justification:
PowerShell provides reproducible Windows-based evidence-management
and project automation.

---

## 2. Python

Purpose:
Automated forensic analysis and evidence processing.

Scripts:
- scripts/phishing_header_analyzer.py
- scripts/extract_malware_iocs.py
- scripts/financial_fraud_analyzer.py
- scripts/generate_hashes.py
- scripts/verify_hashes.py

Justification:
Python enables repeatable extraction, parsing, correlation and
cryptographic verification.

---

## 3. Email Header Analysis

Purpose:
Identify:
- Sender information
- Received IP
- Message-ID
- Authentication results
- Suspicious URLs

Primary Evidence:
phishing_samples/

Justification:
Email headers help investigators reconstruct the source and
characteristics of suspicious messages.

---

## 4. SPF / DKIM / DMARC

Purpose:
Evaluate simulated email sender authentication.

Evidence:
spoofing_analysis/spf_dkim_dmarc_analysis.md

Justification:
These mechanisms help determine whether an email's claimed
sender domain has passed the expected authentication checks.

Note:
The results in this project are simulated rather than live DNS
authentication results.

---

## 5. WHOIS / Domain Investigation

Purpose:
Investigate domain registration and ownership information
during a real-world investigation.

Evidence:
spoofing_analysis/whois_domain_analysis.md

Justification:
WHOIS information can provide useful domain-registration
context and support infrastructure correlation.

Note:
This assignment uses reserved .example domains for simulation.

---

## 6. Malware IOC Extraction

Purpose:
Extract indicators from the simulated malware artifact.

Indicators:
- SHA-256
- C2 domain
- C2 IP
- File path
- Mutex

Evidence:
malware_analysis/extracted_iocs.txt

Justification:
IOCs allow investigators to document and correlate suspicious
artifacts without executing potentially dangerous software.

---

## 7. Financial Transaction Analysis

Purpose:
Analyze simulated payment flows and identify a possible
victim -> mule -> crypto pattern.

Evidence:
financial_fraud/

Justification:
Transaction correlation helps investigators understand
the movement of simulated fraudulent funds.

---

## 8. SHA-256

Purpose:
Verify evidence integrity.

Commands:
python scripts/generate_hashes.py
python scripts/verify_hashes.py

Evidence:
hashes/SHA256SUMS.txt

Justification:
Cryptographic hashes provide a reproducible integrity check
for investigation artifacts.

---

## 9. VirusTotal

Purpose:
In a real defensive investigation, an authorized investigator
may use VirusTotal to check whether a file, URL, domain or hash
has existing security detections.

Safety:
Only non-sensitive and authorized indicators should be submitted.

This project does not upload real malware or private evidence.

---

## 10. MXToolbox

Purpose:
In a real investigation, MXToolbox can assist with DNS, MX,
SPF and related email infrastructure checks.

Safety:
Use only domains that you are authorized to investigate.

---

## 11. AbuseIPDB

Purpose:
In a real investigation, AbuseIPDB can provide reputation/context
for an IP address.

Safety:
The IP addresses in this project are documentation/example ranges,
so they are not treated as real malicious infrastructure.

---

## Investigation Principle

Tools should support evidence-based analysis rather than replace
investigator judgment.

All results must be documented with:
- Source
- Timestamp
- Evidence identifier
- Analysis method
- Limitations


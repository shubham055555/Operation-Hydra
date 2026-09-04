# Operation Hydra

## Assignment 2 - Unit 2: Types of Cyber Crimes

Operation Hydra is an academic simulation of a multi-vector cybercrime
investigation involving phishing, spoofing, simulated malware delivery,
credential compromise and financial fraud.

## Objective

The project demonstrates:

- Phishing investigation
- Email and sender spoofing analysis
- SPF, DKIM and DMARC analysis
- Simulated malware IOC extraction
- Financial fraud tracing
- Mule-account pattern analysis
- Evidence correlation
- SHA-256 evidence integrity
- Legal, ethical and impact analysis

## Safety Notice

All evidence in this repository is synthetic and created for academic use.

No real:
- credentials
- payment cards
- bank accounts
- UPI accounts
- cryptocurrency wallets
- malware
- victims
- malicious infrastructure

are used.

The malware component is an inert text simulation and was not executed.

## Attack Chain

Phishing
  ->
Spoofing
  ->
Suspicious Link or Attachment
  ->
Simulated Trojan / Keylogger
  ->
Credential Compromise
  ->
Financial Fraud
  ->
Simulated Mule Account
  ->
Simulated Cryptocurrency Destination

## Project Structure

- phishing_samples
- spoofing_analysis
- malware_analysis
- financial_fraud
- generated_data
- extracted_artifacts
- hashes
- scripts
- screenshots
- report
- .github/workflows

## Investigation Scripts

- phishing_header_analyzer.py
- extract_malware_iocs.py
- financial_fraud_analyzer.py
- generate_hashes.py
- verify_hashes.py

## Evidence Integrity

SHA-256 hashes are generated and verified using Python scripts.

Hash file:
hashes/SHA256SUMS.txt

## Reports

The report directory contains legal, ethical, impact and investigation
documentation.

## Tools

- PowerShell
- Python
- Email header analysis
- SPF/DKIM/DMARC
- WHOIS methodology
- VirusTotal methodology
- MXToolbox methodology
- AbuseIPDB methodology
- SHA-256

## GitHub Actions

The CI workflow validates:

- Required directories
- Required files
- Markdown files
- Python syntax

Workflow:
.github/workflows/validate.yml

## Authorship

Project: Operation Hydra
Assignment: Assignment 2 - Unit 2
Purpose: Academic Cybercrime Investigation Simulation

## Disclaimer

This repository is intended only for controlled academic and educational
use. No real system, person, account, domain or malicious infrastructure
was targeted.

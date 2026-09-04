# Operation Hydra - Evidence Correlation Timeline

## Incident ID
HYDRA-2026-001

## Attack Timeline

| Time | Event | Evidence | Investigation Finding |
|---|---|---|---|
| 09:00 | Phishing campaign begins | phishing_email_01.txt | Initial social-engineering contact |
| 09:01 | First simulated payment | TXN-001 | Victim-to-mule transfer |
| 09:04 | Second simulated payment | TXN-002 | Repeated victim transaction |
| 09:08 | Third simulated payment | TXN-003 | Multiple victims funnel funds |
| 09:12 | Simulated card transaction | TXN-004 | Payment fraud stage |
| 09:15 | Mule forwards funds | TXN-005 | Mule-to-crypto movement |
| 09:18 | Mule forwards funds | TXN-006 | Continued fund movement |
| 09:21 | Mule forwards funds | TXN-007 | Final simulated crypto transfer |

---

## Evidence Relationships

### 1. Phishing Evidence
Files:
- phishing_email_01.txt
- phishing_email_02.txt
- phishing_email_03.txt

Purpose:
Establishes the simulated initial-access mechanism.

### 2. Spoofing Evidence
File:
- spoofing_analysis/spf_dkim_dmarc_analysis.md

Purpose:
Documents simulated sender-authentication failures.

### 3. Malware Evidence
Files:
- malware_analysis/HydraKeyLogger_simulated.txt
- malware_analysis/extracted_iocs.txt
- malware_analysis/attack_vector_mapping.md

Purpose:
Represents the simulated credential-theft stage.

### 4. Financial Evidence
Files:
- financial_fraud/simulated_transactions.txt
- financial_fraud/fraud_analysis.txt

Purpose:
Demonstrates the simulated movement of fraudulent funds.

---

## Investigative Chain

Phishing
    ->
Spoofing
    ->
Simulated Malware Delivery
    ->
Credential Compromise
    ->
Payment Fraud
    ->
Mule Account
    ->
Simulated Cryptocurrency Destination

---

## Conclusion

The evidence forms a coherent simulated multi-vector cybercrime campaign.
The individual artifacts are correlated through timestamps, attack stages,
simulated identifiers and common campaign ID HYDRA-2026-001.

All evidence remains synthetic and is intended solely for academic analysis.


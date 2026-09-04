from pathlib import Path
import re

BASE = Path(__file__).resolve().parent.parent
SOURCE = BASE / "financial_fraud" / "simulated_transactions.txt"
OUTPUT = BASE / "financial_fraud" / "fraud_analysis.txt"

text = SOURCE.read_text(encoding="utf-8")

amounts = [
    int(x)
    for x in re.findall(r"\b(\d{4,6})\b", text)
    if 1000 <= int(x) <= 100000
]

victim_to_mule = len(
    re.findall(r"VICTIM-SIM-\d+\s+MULE-SIM-01", text)
)

mule_to_crypto = len(
    re.findall(r"MULE-SIM-01\s+CRYPTO-SIM-01", text)
)

wallet = re.search(r"Address:\s*(.+)", text)
wallet_value = wallet.group(1).strip() if wallet else "Not found"

report = f"""OPERATION HYDRA - FINANCIAL FRAUD ANALYSIS
================================================

Data Type: Synthetic / Academic Simulation

Victim-to-Mule Transactions: {victim_to_mule}
Mule-to-Crypto Transactions: {mule_to_crypto}

Simulated Crypto Address:
{wallet_value}

Key Findings
------------
1. Multiple simulated victims transfer funds to MULE-SIM-01.
2. The intermediate account receives several transactions in a short period.
3. MULE-SIM-01 subsequently transfers funds to CRYPTO-SIM-01.
4. Similar transaction values create a simulated funneling pattern.
5. The pattern is consistent with a hypothetical mule-account workflow.

Investigation Classification
----------------------------
Initial Stage: Phishing / Credential Theft Simulation
Financial Stage: Payment Fraud Simulation
Intermediate Node: MULE-SIM-01
Final Destination: CRYPTO-SIM-01

Important Limitation
--------------------
All accounts, transaction IDs, amounts and wallet identifiers are synthetic.
No real financial activity occurred.

Recommended Evidence Correlation
--------------------------------
- Email headers
- Phishing URLs
- Malware IOCs
- Transaction timestamps
- Simulated account identifiers
- Simulated cryptocurrency destination

"""

OUTPUT.write_text(report, encoding="utf-8")

print("Financial fraud analysis completed.")
print(f"Output: {OUTPUT}")

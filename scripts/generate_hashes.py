from pathlib import Path
import hashlib

BASE = Path(__file__).resolve().parent.parent
HASH_DIR = BASE / "hashes"

TARGETS = [
    BASE / "generated_data" / "incident_scenario.txt",
    BASE / "generated_data" / "cybercrime_mapping.md",

    BASE / "phishing_samples" / "phishing_email_01.txt",
    BASE / "phishing_samples" / "phishing_email_02.txt",
    BASE / "phishing_samples" / "phishing_email_03.txt",

    BASE / "spoofing_analysis" / "spf_dkim_dmarc_analysis.md",
    BASE / "spoofing_analysis" / "whois_domain_analysis.md",

    BASE / "malware_analysis" / "HydraKeyLogger_simulated.txt",
    BASE / "malware_analysis" / "extracted_iocs.txt",
    BASE / "malware_analysis" / "attack_vector_mapping.md",

    BASE / "financial_fraud" / "simulated_transactions.txt",
    BASE / "financial_fraud" / "fraud_analysis.txt",
    BASE / "financial_fraud" / "evidence_correlation.md",
]

HASH_DIR.mkdir(parents=True, exist_ok=True)

output = []

for file_path in TARGETS:
    if not file_path.exists():
        output.append(f"NOT FOUND | {file_path.relative_to(BASE)}")
        continue

    sha256 = hashlib.sha256(file_path.read_bytes()).hexdigest()
    relative = file_path.relative_to(BASE)

    output.append(f"{sha256}  {relative}")

hash_file = HASH_DIR / "SHA256SUMS.txt"
hash_file.write_text("\n".join(output) + "\n", encoding="utf-8")

print(f"SHA-256 hashing completed.")
print(f"Hash file: {hash_file}")
print(f"Artifacts processed: {len(TARGETS)}")

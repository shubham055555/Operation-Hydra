from pathlib import Path
import re

BASE = Path(__file__).resolve().parent.parent
EMAIL_DIR = BASE / "phishing_samples"
OUTPUT = BASE / "spoofing_analysis" / "header_analysis.txt"

results = []

for email_file in sorted(EMAIL_DIR.glob("phishing_email_*.txt")):
    text = email_file.read_text(encoding="utf-8")

    received_ips = re.findall(
        r"Received:.*?\((\d{1,3}(?:\.\d{1,3}){3})\)",
        text,
        re.IGNORECASE
    )

    urls = re.findall(r"https?://[^\s]+", text)

    auth = re.search(
        r"Authentication-Results:\s*(.+)",
        text,
        re.IGNORECASE
    )

    from_match = re.search(
        r"^From:\s*(.+)",
        text,
        re.MULTILINE
    )

    subject_match = re.search(
        r"^Subject:\s*(.+)",
        text,
        re.MULTILINE
    )

    results.append("=" * 70)
    results.append(f"FILE: {email_file.name}")
    results.append(f"FROM: {from_match.group(1) if from_match else 'Not found'}")
    results.append(f"SUBJECT: {subject_match.group(1) if subject_match else 'Not found'}")
    results.append(
        f"IP ADDRESSES: {', '.join(received_ips) if received_ips else 'Not found'}"
    )
    results.append(
        f"URLS: {', '.join(urls) if urls else 'Not found'}"
    )
    results.append(
        f"AUTHENTICATION: {auth.group(1) if auth else 'Not found'}"
    )
    results.append("ASSESSMENT: Suspicious simulated phishing message")
    results.append("")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text("\n".join(results), encoding="utf-8")

print(f"Analyzed {len(list(EMAIL_DIR.glob('phishing_email_*.txt')))} email samples.")
print(f"Report written to: {OUTPUT}")

from pathlib import Path
import hashlib

BASE = Path(__file__).resolve().parent.parent
HASH_FILE = BASE / "hashes" / "SHA256SUMS.txt"

passed = 0
failed = 0

for line in HASH_FILE.read_text(encoding="utf-8").splitlines():

    line = line.strip()

    if not line:
        continue

    parts = line.split(maxsplit=1)

    if len(parts) != 2:
        print(f"SKIP | Invalid hash entry: {line}")
        continue

    expected = parts[0]
    relative = parts[1].strip()

    file_path = BASE / relative

    if not file_path.exists():
        print(f"FAIL | {relative} | File missing")
        failed += 1
        continue

    actual = hashlib.sha256(file_path.read_bytes()).hexdigest()

    if actual == expected:
        print(f"PASS | {relative}")
        passed += 1
    else:
        print(f"FAIL | {relative} | Hash mismatch")
        failed += 1

print()
print("=" * 60)
print(f"Verification Summary: {passed} PASS / {failed} FAIL")
print("=" * 60)

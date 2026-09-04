# Operation Hydra - SPF / DKIM / DMARC Analysis

## Investigation Scope

The following three email samples were created for academic simulation:

1. phishing_email_01.txt
2. phishing_email_02.txt
3. phishing_email_03.txt

No real phishing infrastructure or victim accounts were used.

---

## Email 01

Sender Domain:
hydra-bank.example

Observed Sending IP:
192.0.2.10

SPF:
FAIL

DKIM:
FAIL

DMARC:
FAIL

Assessment:
The simulated message fails all three sender-authentication checks.
This indicates that the displayed sender identity cannot be trusted
based on the simulated authentication results.

---

## Email 02

Sender Domain:
hydra-pay.example

Observed Sending IP:
198.51.100.25

SPF:
SOFTFAIL

DKIM:
FAIL

DMARC:
FAIL

Assessment:
The simulated sender has an SPF soft failure and failed DKIM/DMARC
authentication. The combination is treated as suspicious.

---

## Email 03

Sender Domain:
hydra-security.example

Observed Sending IP:
203.0.113.45

SPF:
FAIL

DKIM:
FAIL

DMARC:
FAIL

Assessment:
The simulated message fails SPF, DKIM and DMARC. The sender identity
should therefore be treated as untrusted within this simulation.

---

## Overall Finding

All three simulated phishing messages contain authentication failures
consistent with sender/domain impersonation.

The IP addresses belong to documentation/example ranges and are not
treated as real malicious infrastructure.

## Investigation Limitation

SPF, DKIM and DMARC results in these email samples are intentionally
simulated. They are not live DNS authentication results.

For a real investigation, the investigator would validate the domain's
DNS records and email authentication results using authorized forensic
and DNS-analysis tools.


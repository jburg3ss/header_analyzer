from pathlib import Path

from header_analyzer.core.parsers.authentication import parse_authentication_results
from header_analyzer.core.parsers.canonical import parse_headers

PROJECT_ROOT = Path(__file__).parent.parent
SAMPLES = PROJECT_ROOT / "src" / "header_analyzer" / "data" / "sample_headers" / "phishing_headers.txt"


with open(SAMPLES) as h:
    headers = parse_headers(h.read())

# Step 1: Parse with canonical parser
print("After canonical.parse_headers():")
print(f"Keys: {list(headers.keys())}")
print("\nAuthentication-Results value:")
print(repr(headers["Authentication-Results"][0]))
print()

# Step 2: Parse authentication results
auth_header = headers["Authentication-Results"][0]
result = parse_authentication_results(auth_header)

print("After parse_authentication_results():")
print(f"Server: {result['server']}")
print(f"SPF:    {result['spf']}")
print(f"DKIM:   {result['dkim']}")
print(f"DMARC:  {result['dmarc']}")

# TODO: Remove AI crap and do this yourself

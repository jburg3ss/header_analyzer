<!-- docs/parsers/canonical.md -->

## Canonical

### Overview
The canonical parser is a thin wrapper around Python's built-in [`email`](https://docs.python.org/3/library/email.html) package.  
It defines a single function, `parse_headers()`, which parses raw email header data into a RFC-5322 compliant structure for downstream analysis.

This function guarantees:
- Correct RFC-5322 field parsing (delegated to the email stdlib)
- Canonical field-name casing (`from` → `From`, `content-type` → `Content-Type`)
- Consistent unfolding of continuation lines
- Preservation of repeated headers and their order
- Safe handling of both `str` and `bytes` inputs

### Features
| Features | Description | Example |
|------------|--------------|----------|
| **Canonical casing** | Known headers are normalized via an internal lookup (`_FIELD`), unknown headers are Title-Cased. | `x-custom-header` --> `X-Custom-Header` |
| **Unfolding** | Continuation lines starting with space or tab are automatically joined by `email.policy.default`. | `"X-Note: Foo\r\n Bar"` --> `"Foo Bar"` |
| **Repeated fields** | Multiple headers with the same name, (e.g., `Received`), are preserved in input order. | `{'Received': ['relay1', 'relay2']}` |
| **Input types** | `bytes` input is decoded as UTF-8 using `surrogateescape`. Output is always a `dict[str, list[str]]`. | Both input types produce identical output. |

#### Line Endings
The parser accepts CRLF (`\r\n`), CR (`\r`), and LF (`\n`). All line endings are normalized to LF internally. This ensures consistent behavior across systems: Windows uses CRLF, Unix uses LF, and older Mac systems used CR.

---
### Example
```python
from header_analyzer.core.parsers.canonical import parse_headers

raw = (
    "FROM: det_connors@fbi.gov\r\n"
    "subject:  Test  \r\n"
    "received: relay1\r\n"
    "received: relay2\r\n"
)

headers = parse_headers(raw)
print(headers)
# {
#   "From": ["det_connors@fbi.gov"],
#   "Subject": ["Test"],
#   "Received": ["relay1", "relay2"]
# }
```

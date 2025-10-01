# src/header_analyzer/core/parsers/canonical.py

"""
Normalizes raw email headers into a consistent structure for safe analysis.

Handles:
    - Line ending normalization (CRLF/CR → LF)
    - Unfolding wrapped lines (continuation lines starting with space/tab)
    - Header name standardization (FROM/from → From per RFC 5322)
    - Preserving multiple instances of the same header in order
    - Removing NULs and excess whitespace

References:
    ~ https://datatracker.ietf.org/doc/html/rfc5322#section-3.2.2
    ~ https://datatracker.ietf.org/doc/html/rfc5322#section-4.1
"""


class CanonicalHeaders:
    pass



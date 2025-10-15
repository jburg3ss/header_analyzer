# src/header_analyzer/core/parsers/canonical.py

"""
Parses email headers and normalizes their field names to meet RFC 5322
compliance.

- The email module--specifically, email.policy--takes care of additional parsing
  (unfolding, decoding, line endings etc)
- canonicalize_header() normalizes all headers to consistent case for clean
  analysis output

References:
    - https://datatracker.ietf.org/doc/html/rfc5322
"""

from email import policy
from email.parser import HeaderParser

_FIELD = {
    "from": "From",
    "to": "To",
    "cc": "Cc",
    "bcc": "Bcc",
    "subject": "Subject",
    "date": "Date",
    "message-id": "Message-ID",
    "in-reply-to": "In-Reply-To",
    "references": "References",
    "reply-to": "Reply-To",
    "sender": "Sender",
    "return-path": "Return-Path",
    "received": "Received",
    "content-type": "Content-Type",
    "content-transfer-encoding": "Content-Transfer-Encoding",
    "mime-version": "MIME-Version",
    "keywords": "Keywords",
    "comments": "Comments",
    "resent-date": "Resent-Date",
    "resent-from": "Resent-From",
    "resent-sender": "Resent-Sender",
    "resent-to": "Resent-To",
    "resent-cc": "Resent-Cc",
    "resent-bcc": "Resent-Bcc",
    "resent-message-id": "Resent-Message-ID",
    "x-mailer": "X-Mailer",
    "list-unsubscribe": "List-Unsubscribe",
    "authentication-results": "Authentication-Results",
    "dkim-signature": "DKIM-Signature",
    "received-spf": "Received-SPF",
}


def canonicalize_header(name: str) -> str:
    """
    Return RFC-ish canonical case for a non-empty header name.

    Args:
        name: Raw header field name (e.g., "FROM", "content-TYPE")

    Returns:
        Canonical form (e.g., "From", "Content-Type")

    Examples:
        >>> canonicalize_header("FROM")
        "From"

        >>> canonicalize_header("x-custom-header")
        "X-Custom-Header"
    """

    key = name.strip().lower()
    return _FIELD.get(key, "-".join(seg.capitalize() for seg in key.split("-")))


def parse_headers(raw: str | bytes) -> dict[str, list[str]]:
    """
    Parse raw headers using the Python standard library.

    Returns:
        dict[str, list[str]]: Canonical header names mapped to their values,
        preserving order and allowing multiple values per field.
    """

    if isinstance(raw, bytes):
        text = raw.decode("utf-8", errors="surrogateescape")
    else:
        text = raw

    parser = HeaderParser(policy=policy.default)
    parsed_headers = parser.parsestr(text)

    headers: dict[str, list[str]] = {}
    for h_name, h_value in parsed_headers.items():
        if not h_name.strip():
            continue
        cname = canonicalize_header(h_name)
        headers.setdefault(cname, []).append(h_value.strip())

    return headers

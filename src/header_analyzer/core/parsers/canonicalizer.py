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
    ~ https://datatracker.ietf.org/doc/html/rfc5321
    ~ https://datatracker.ietf.org/doc/html/rfc5322
    ~ https://datatracker.ietf.org/doc/html/rfc3469
    ~ https://datatracker.ietf.org/doc/html/rfc6376
    ~ https://datatracker.ietf.org/doc/html/rfc7208
    ~ https://datatracker.ietf.org/doc/html/rfc8601
"""

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
    Desc:
        Canonical header field name to RFC 5322 case (FROM:/from: -> From:)

    Args: 
        name: Raw header field name (e.g., "FROM", "content-TYPE")

    Returns: 
        Canonical form (e.g., "From", "Content-Type"), or empty string if invalid

    Examples:
        >>> canonicalize_header("FROM")
        "From"

        >>> canonicalize_header("x-custom-header")
        "X-Custom-Header"
    """

    key = name.strip().lower()
    if not key:
        return ""
    
    return _FIELD.get(key, "-".join(f.capitalize() for f in key.split("-")))












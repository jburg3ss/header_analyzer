# src/header_analyzer/core

from email.parser import BytesParser
from email.policy import default
from email.utils import parseaddr

from header_analyzer.core.models import StandardHeaders


def parse_headers(raw: bytes) -> StandardHeaders:
    """
    Parse raw email text into a StandardHeaders dataclass.
        :param raw: Raw email text
        :return: Parsed headers wrapped in a StandardHeaders instance
    """
    msg = BytesParser(policy=default).parsebytes(raw)

    # Extract the domain part from the From header only.
    _, email_addr = parseaddr(msg.get("From", ""))
    from_domain = email_addr.split("@")[-1] if "@" in email_addr else ""

    return StandardHeaders(
        from_=msg.get("From", ""),
        to=msg.get("To", ""),
        subject=msg.get("Subject", ""),
        date=msg.get("Date", ""),
        message_id=msg.get("Message-ID", ""),
        received=msg.get_all("Received", []) or [],
        return_path=msg.get("Return-Path"),
        from_domain=from_domain,
        reply_to=msg.get("Reply-To"),
        auth_results=msg.get("Authentication-Results"),
    )


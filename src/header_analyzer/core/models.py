"""

"""

from __future__ import annotations
from dataclasses import dataclass

@dataclass(slots=True)
class StandardHeaders:
    """
    https://datatracker.ietf.org/doc/html/rfc5322

    :param from_: Full "From" header value, with name and address (str)
    :param to: Raw "To" header value, may include multiple recipients (str)
    :param subject: Subject line of the email (str)
    :param date: "Date" header string, when the message was sent (str)
    :param message_id: Unique "Message-ID" identifier (str)
    :param received: Delivery chain via "Received" headers (list[str])
    :param return_path: "Return-Path" header, bounce address (str)
    :param from_domain: Domain extracted from "From" address (str)

    :param reply_to: "Reply-To" header address if present. Optional.
    :param auth_results: Authentication results (SPF/DKIM/DMARC etc). Optional 

    """
    from_: str
    to: str
    subject: str
    date: str
    message_id: str
    received:  list[str]
    return_path: str | None
    from_domain: str
    reply_to: str | None
    auth_results: str | None 

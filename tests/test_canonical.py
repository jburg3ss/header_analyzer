# tests/test_canonical.py

import pytest

from header_analyzer.core.parsers.canonical import canonicalize_header


@pytest.mark.parametrize(
    "header,expected",
    [
        ("from", "From"),
        ("content-type", "Content-Type"),
        ("content-transfer-encoding", "Content-Transfer-Encoding"),
        ("message-id", "Message-ID"),
        ("x-mailer", "X-Mailer"),
        ("resent-message-id", "Resent-Message-ID"),
        ("authentication-results", "Authentication-Results"),
        ("received-spf", "Received-SPF"),
    ],
)
def test_known_headers(header, expected):
    """

    :param header: param expected:
    :param expected:

    """
    assert canonicalize_header(header) == expected

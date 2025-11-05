# tests/test_parse_headers.py

import pytest

from header_analyzer.core.parsers.canonical import parse_headers

@pytest.mark.parametrize(
    "raw,expected_key,expected_value",
    [
        ("From: alice@example.com", "From", "alice@example.com"),
        ("from: alice@example.com", "From", "alice@example.com"),
        ("Content-Type: text/html", "Content-Type", "text/html"),
        ("X-Mailer: Test", "X-Mailer", "Test"),
        ("Subject:  Test  ", "Subject", "Test"),
    ],
)
def test_parse_single_header(
        raw: str, expected_key: 
        str, expected_value: 
        str
) -> None:
    """
    :param raw: str:
    :param expected_key: str:
    :param expected_value: str:
    """
    result = parse_headers(raw)
    assert result[expected_key] == [expected_value]

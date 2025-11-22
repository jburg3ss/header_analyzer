"""Parses email authentication headers (Authentication-Results, DKIM-Signature, etc.) to
extract security-relevant metadata.

Authentication-Results headers contain the results of email authentication checks
performed by the receiving mail server (SPF, DKIM, DMARC, ARC).

References:
    - RFC 8601: Authentication-Results Header Field
      https://datatracker.ietf.org/doc/html/rfc8601
    - RFC 6376: DKIM Signatures
      https://datatracker.ietf.org/doc/html/rfc6376
    - RFC 7489: DMARC
      https://datatracker.ietf.org/doc/html/rfc7489

Note:
    Header values are pre-processed by canonical.py (unfolded, decoded, normalized)
    before reaching these parsers.

"""

from typing import TypedDict


class AuthenticationResult(TypedDict):
    method: str
    result: str


class AuthenticationResultsData(TypedDict):
    authserv_id: str
    results: list[AuthenticationResult]


# def parse_authentication_results(
#     auth_header: str,
# ) -> AuthenticationResultsData:
#     """Parse an Authentication-Results header into structured data.
#
#     Authentication-Results headers have the format:
#         authserv-id; method1=result1; method2=result2; ...
#
#     Example:
#         mx.google.com; spf=pass smtp.mailfrom=example.com; dkim=pass
#
#     Example:
#
#     >>> parse_authentication_results("mx.google.com; spf=pass; dkim=pass")
#         {
#             "authserv_id": "mx.google.com",
#             "results": [
#                 {"method": "spf", "result": "pass"},
#                 {"method": "dkim", "result": "pass"}
#             ]
#         }
#
#     """
#
#     if not auth_header:
#         return {"authserv_id": "", "results": []}
#
#     return auth_header
#     # return {"authserv_id": "", "results": []}

def parse_authentication_results(auth_header: str) -> AuthenticationResultsData:
    if not auth_header:
        return {"authserv_id": "", "results": []}

    parts = [p.strip() for p in auth_header.split(";")]
    authserv_id = parts[0]

    results: list[AuthenticationResult] = []

    for part in parts[1:]:
        if "=" not in part:
            continue
        method, result = part.split("=", 1)
        results.append({"method": method.strip(), "result": result.strip()})

    return {"authserv_id": authserv_id, "results": results}

# header_analyzer

A tool for analyzing email headers to determine whether a message is legitimate or suspicious. It focuses on header-only analysis (no body parsing) and uses authentication checks, routing analysis, and anomaly detection to flag inconsistencies.

I wanted something quick and convenient for work, where I could just copy/paste headers into a window and get a detailed breakdown of the email's routing, authentication results, and any suspicious anomalies.

## Features

**Authentication Checks**

Validates SPF, DKIM, DMARC, and ARC to verify the sender's identity and that the message hasn't been tampered with during transit.

**Identity Consistency**

Compares From, Reply-To, Sender, and Return-Path fields to catch mismatches—like when an email claims to be from PayPal but replies go to scam.com. Also validates Message-ID format and detects legitimate bulk mail indicators.

**Routing Analysis**

Traces the email's path through Received headers, checking for logical hop order, missing relays, and timestamp inconsistencies. Includes reverse DNS lookups and TLS status when available.

**Domain & Integrity**

Flags domain alignment issues, homoglyph attacks (rnicrosoft.com vs microsoft.com), punycode tricks, and malformed or duplicate headers.

**Trust Scoring**

Combines all checks into a weighted score.

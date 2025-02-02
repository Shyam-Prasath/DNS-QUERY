# DNS Query Tool

A Python-based DNS query tool that retrieves various DNS records for a given domain.

## Features

- Query different types of DNS records:
  - A (IPv4 address)
  - AAAA (IPv6 address)
  - MX (Mail Exchange)
  - NS (Name Server)
  - TXT (Text)
  - CNAME (Canonical Name)
  - SOA (Start of Authority)
  - SRV (Service)
  - PTR (Reverse DNS lookup)

## Requirements

Ensure you have Python installed (version 3.x recommended). Install the required dependency:

```sh
pip install dnspython
```

## Usage

Run the script and provide a domain name as input:

```sh
python dns_query_tool.py
```

### Example Queries

1. **A Record**
   - Input: `example.com`
   - Output: `['93.184.216.34']`

2. **MX Record**
   - Input: `gmail.com`
   - Output: `[(10, 'alt1.gmail-smtp-in.l.google.com')]`

3. **PTR Record** (Reverse DNS lookup)
   - Input: `8.8.8.8`
   - Output: `['dns.google']`

## Code Structure

- `DNSQueryTool` class handles DNS queries.
- Methods correspond to different record types.
- The script takes user input for domain/IP and prints results.

## Author

Shyam Prasath


import dns.resolver
import dns.query
import dns.dnssec
import dns.message
import dns.name
import dns.rdatatype
import dns.exception

class DNSQueryTool:
    def __init__(self, domain):
        self.domain = domain

    def query_a_record(self):
        """Query A (IPv4) records for the domain."""
        try:
            answers = dns_query_tool.resolver.resolve(self.domain, 'A')
            return [rdata.address for rdata in answers]
        except dns_query_tool.exception.DNSException as e:
            return f"Error querying A record: {e}"

    def query_aaaa_record(self):
        """Query AAAA (IPv6) records for the domain."""
        try:
            answers = dns_query_tool.resolver.resolve(self.domain, 'AAAA')
            return [rdata.address for rdata in answers]
        except dns_query_tool.exception.DNSException as e:
            return f"Error querying AAAA record: {e}"

    def query_mx_record(self):
        """Query MX (Mail Exchange) records for the domain."""
        try:
            answers = dns_query_tool.resolver.resolve(self.domain, 'MX')
            return [(rdata.preference, rdata.exchange.to_text()) for rdata in answers]
        except dns_query_tool.exception.DNSException as e:
            return f"Error querying MX record: {e}"

    def query_ns_record(self):
        """Query NS (Name Server) records for the domain."""
        try:
            answers = dns_query_tool.resolver.resolve(self.domain, 'NS')
            return [rdata.target.to_text() for rdata in answers]
        except dns_query_tool.exception.DNSException as e:
            return f"Error querying NS record: {e}"

    def query_txt_record(self):
        """Query TXT (Text) records for the domain."""
        try:
            answers = dns_query_tool.resolver.resolve(self.domain, 'TXT')
            return [rdata.strings for rdata in answers]
        except dns_query_tool.exception.DNSException as e:
            return f"Error querying TXT record: {e}"

    def query_cname_record(self):
        """Query CNAME (Canonical Name) records for the domain."""
        try:
            answers = dns_query_tool.resolver.resolve(self.domain, 'CNAME')
            return [rdata.target.to_text() for rdata in answers]
        except dns_query_tool.exception.DNSException as e:
            return f"Error querying CNAME record: {e}"

    def query_soa_record(self):
        """Query SOA (Start of Authority) record for the domain."""
        try:
            answers = dns_query_tool.resolver.resolve(self.domain, 'SOA')
            for rdata in answers:
                return {
                    'Primary NS': rdata.mname.to_text(),
                    'Responsible Email': rdata.rname.to_text(),
                    'Serial': rdata.serial,
                    'Refresh': rdata.refresh,
                    'Retry': rdata.retry,
                    'Expire': rdata.expire,
                    'Minimum TTL': rdata.minimum
                }
        except dns_query_tool.exception.DNSException as e:
            return f"Error querying SOA record: {e}"

    def query_srv_record(self):
        """Query SRV (Service) records for the domain."""
        try:
            answers = dns_query_tool.resolver.resolve(self.domain, 'SRV')
            return [(rdata.priority, rdata.weight, rdata.port, rdata.target.to_text()) for rdata in answers]
        except dns_query_tool.exception.DNSException as e:
            return f"Error querying SRV record: {e}"

    def query_ptr_record(self, ip_address):
        """Query PTR (Reverse DNS) records for an IP address."""
        try:
            reversed_name = dns_query_tool.reversename.from_address(ip_address)
            answers = dns_query_tool.resolver.resolve(reversed_name, 'PTR')
            return [rdata.target.to_text() for rdata in answers]
        except dns_query_tool.exception.DNSException as e:
            return f"Error querying PTR record: {e}"

# Example usage:
if __name__ == "__main__":
    domain = input("Enter a domain: ")
    dns_tool = DNSQueryTool(domain)

    print("A Record:", dns_tool.query_a_record())
    print("AAAA Record:", dns_tool.query_aaaa_record())
    print("MX Record:", dns_tool.query_mx_record())
    print("NS Record:", dns_tool.query_ns_record())
    print("TXT Record:", dns_tool.query_txt_record())
    print("CNAME Record:", dns_tool.query_cname_record())
    print("SOA Record:", dns_tool.query_soa_record())
    print("SRV Record:", dns_tool.query_srv_record())

    # Example for PTR record (reverse DNS lookup)
    ip_address = input("Enter an IP address for reverse lookup (PTR record): ")
    print("PTR Record:", dns_tool.query_ptr_record(ip_address))

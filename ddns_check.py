import requests
import dns.resolver
import argparse


def main(hostname: str, nameserver: str):
    # Get current IP from host connection
    current_ip = requests.get("https://ifconfig.me/").text

    # Initialize and configure DNS Resolver
    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = [nameserver]

    # Query DNS Resolver for specified hostname
    dns_answer = my_resolver.resolve(hostname)

    # Verify that DNS Result and Current IP matches
    if dns_answer[0].to_text() == current_ip:
        print(f"DDNS result matches current IP Address ({dns_answer[0].to_text()})")
        raise SystemExit(0)
    else:
        print("DDNS result and current IP Address mismatch!\n"
              "Current IP: {current_ip}\n"
              "DDNS Result: {dns_answer[0].to_text()}")
        raise SystemExit(2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("hostname")
    parser.add_argument("nameserver")
    args = parser.parse_args()

    main(args.hostname, args.nameserver)

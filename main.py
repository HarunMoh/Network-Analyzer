from capture import start_capture, captured_ips
from analyzer import show_statistics
from ipwhois import lookup_ip


def main():
    print("=== Network Traffic Analyzer ===")
 
    # control how long the capture should runs
    start_capture(duration=3)

    # shows the statistics of the captured packets
    show_statistics()

    # sort the found ip addresses and look them up
    print("\n=== IP Address Identification ===")

    # loop through the captured IPs, look them up, and print the results to reduce the number of requests to the API
    for ip in sorted(captured_ips):
        info = lookup_ip(ip)

        print(f"\nIP Address: {ip}")
        print(f"Hostname: {info['hostname']}")
        print(f"Organization: {info['organization']}")


if __name__ == "__main__":
    main()

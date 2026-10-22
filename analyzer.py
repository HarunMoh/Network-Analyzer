from collections import defaultdict

# each protocol maintains its own packet and byte counters
protocol_stats = defaultdict(
    lambda: {"packets": 0, "bytes": 0}
)

def analyze_packet(protocol, packet_size):
    
    # increase the packet and byte counters for the given protocol
    protocol_stats[protocol]["packets"] += 1
    
    # apply the packet size to the byte counter for the given protocol
    protocol_stats[protocol]["bytes"] += packet_size


def show_statistics():
    
    # calculate the total number of packets captured across all protocols
    total_packets = sum(
        data["packets"] for data in protocol_stats.values()
    )
    
    # Track how many packets and bytes each source IP sends.
    ip_stats = defaultdict(
    lambda: {"packets": 0, "bytes": 0}
)

    print("\n=== Protocol Statistics ===")

    # stop the function from tyring to divide by zero if nothing is captured
    if total_packets == 0:
        print("No packets captured.")
        return

    # calculate the percentage of packets for each protocol and print the statistics
    for protocol, data in protocol_stats.items():
        percentage = data["packets"] / total_packets * 100

        print(
            f"{protocol}: "
            f"{data['packets']} packets | "
            f"{data['bytes']} bytes | "
            f"{percentage:.2f}%"
        )

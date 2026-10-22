from scapy.all import sniff, IP, TCP, UDP, ICMP
from analyzer import analyze_packet

captured_ips = set()

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # store ip addresses
        captured_ips.add(src_ip)
        captured_ips.add(dst_ip)

        # sort packets by protocol
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = "Other"

        # packet size and stats
        packet_size = len(packet)
        analyze_packet(protocol, packet_size)

        # prints out packets info
        print(
            f"{src_ip} -> {dst_ip} | "
            f"Protocol: {protocol} | "
            f"Size: {packet_size} bytes"
        )

def start_capture(duration=0, interface=None):
    captured_ips.clear()
    print("------------Collecting Packetss---------------")

    # sniff packets on the specified interface for the given duration
    sniff(
        iface=interface,
        prn=packet_callback,
        store=False,
        timeout=duration
    )


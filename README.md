# Network Traffic Analyzer

A Python-based network traffic analyzer I built to better understand how devices communicate over a network.

The program uses Scapy to capture live network packets, identify common protocols, and analyze traffic statistics. I also added IP address lookups to identify hostnames and organizations associated with captured network traffic.

## Features

- **Live Packet Capture:** Captures network traffic using Scapy and displays the source IP, destination IP, protocol, and packet size.
- **Protocol Statistics:** Tracks TCP, UDP, ICMP, and other IPv4 traffic, including packet counts, total bytes, and percentages.
- **IP Identification:** Uses reverse DNS to identify hostnames and RDAP to retrieve network registration information.
- **WHOIS Lookup:** Provides a Whois.com link for public IP addresses for further investigation.
- **IP Address Classification:** Distinguishes private, public, and multicast IP addresses.
- **Capture Duration:** Allows packets to be captured for a specified amount of time.

## Technologies Used

- Python
- Scapy
- Socket (reverse DNS)
- Requests (RDAP lookups)
- ipaddress
- Npcap (Windows packet capture)

## Project Structure

```text
Network-Traffic-Analyzer/
├── main.py
├── capture.py
├── analyzer.py
├── ipwhois.py
├── requirements.txt
└── README.md
```

**File descriptions:**

- `main.py` — Runs the analyzer and displays the results.
- `capture.py` — Captures packets and extracts network information.
- `analyzer.py` — Calculates protocol statistics and traffic distribution.
- `ipwhois.py` — Handles hostname resolution, IP classification, and RDAP lookups.

## Installation

Make sure Python is installed. On Windows, you'll also need [Npcap](https://npcap.com/#download) to capture network packets.

### 1. Clone the repository

```bash
git clone https://github.com/HarunMoh/Network-Traffic-Analyzer.git
cd Network-Traffic-Analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the analyzer

```bash
python main.py
```

Depending on your operating system and network configuration, you may need administrator privileges to capture packets.

## Example Output

The analyzer displays information about packets as they're captured:

```text
192.168.1.69 -> 140.82.113.21 | Protocol: TCP | Size: 74 bytes
192.168.1.69 -> 239.255.255.250 | Protocol: UDP | Size: 192 bytes
```

After the capture finishes, it summarizes the traffic:

```text
=== Protocol Statistics ===
TCP: 629 packets | 355905 bytes | 84.54%
UDP: 113 packets | 23921 bytes | 15.19%
Other: 2 packets | 130 bytes | 0.27%
```

The program also attempts to identify captured IP addresses:

```text
IP Address: 140.82.113.21
Hostname: lb-140-82-113-21-iad.github.com
Organization: GitHub, Inc.
WHOIS Lookup: https://www.whois.com/whois/140.82.113.21
```

*These examples are illustrative. Actual results depend on the captured traffic and available DNS/RDAP records.*

## How It Works

The program starts by capturing packets from a network interface using Scapy. For each IPv4 packet, it extracts the source and destination IP addresses, identifies the protocol, and records the packet size.

The analyzer uses this information to calculate protocol statistics, including the number of packets, total bytes, and percentage of traffic associated with each protocol.

After the capture finishes, the program performs reverse DNS and RDAP lookups to gather additional information about the IP addresses it detected.

During testing, I noticed that not every IP address has an associated hostname. Some addresses also belong to local network services rather than public servers, so I added checks to distinguish between public, private, and multicast addresses.

## Future Improvements

There are a few features I'd like to add as I continue working on the project:

- Add filtering by IP address, protocol, and port.
- Create charts for protocol distribution and traffic volume.
- Export capture statistics to CSV or JSON.
- Track incoming and outgoing bandwidth.
- Add basic alerts for unusual traffic patterns.

## What I Learned

This project helped me get more comfortable working with Python networking libraries and understanding how network traffic is captured and analyzed.

It also gave me a better understanding of TCP/IP communication, reverse DNS, and how IP registration information can be useful when investigating network connections.

One thing I found interesting was how much background network traffic a computer generates, even when I'm not actively using applications.

## Disclaimer

This project is intended for learning and network troubleshooting. Packet capture should only be performed on networks and systems where you have permission to monitor traffic.

## Author

Harun Mohamed


import socket
import ipaddress
import requests
from functools import lru_cache


@lru_cache(maxsize=1024)
def lookup_ip(ip):
    
    # check if the ip address is a valid public ip
    address = ipaddress.ip_address(ip)

    # if the ip address is not a public ip, return a message indicating that
    if not address.is_global:
        return {
            "hostname": "Local or reserved address",
            "organization": "Not a public IP"
        }
        
    # try to get the hostname and organization using socket and requests libraries
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror, OSError):
        hostname = "Unknown"

    try:
        response = requests.get(
            f"https://rdap.org/ip/{ip}",
            timeout=5
        )
        response.raise_for_status()
        
        # change the response to json format and get the organization name
        data = response.json()

        organization = data.get("name", "Unknown")

    except requests.RequestException:
        organization = "Unknown"

    # return the hostname and organization as a dictionary
    return {
        "hostname": hostname,
        "organization": organization
    }

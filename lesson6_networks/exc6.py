from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
import sys
sys.path.insert(0, '.')  # ignore
from create_recording import recording_path  # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_domain_ip_address():
    packets = rdpcap(recording_path)

    for pkt in packets:
        if pkt.haslayer(DNS):
            dns_layer = pkt[DNS]

            # Check if it's a response and it has a query and an answer
            if dns_layer.qr == 1 and dns_layer.qd is not None and dns_layer.an is not None:
                domain = dns_layer.qd.qname.decode()
                ip_address = dns_layer.an.rdata
                print("Domain:", domain)
                print("IP Address:", ip_address)
                break

show_domain_ip_address()

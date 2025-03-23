from scapy.all import *
from scapy.layers.http import *
import sys
sys.path.insert(0, '.')  # ignore
from create_recording import recording_path

def show_source_destination_ports():
    packets = rdpcap(recording_path)

    # Destination port of 3rd packet (index 2)
    if len(packets) >= 3 and packets[2].haslayer(TCP):
        dst_port = packets[2][TCP].dport
        print("Destination port (3rd packet):", dst_port)

    # Source port of 4th packet (index 3)
    if len(packets) >= 4 and packets[3].haslayer(TCP):
        src_port = packets[3][TCP].sport
        print("Source port (4th packet):", src_port)

show_source_destination_ports()

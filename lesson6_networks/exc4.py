from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_source_destination_ip_address():
    packets = rdpcap(recording_path)  # Load the pcap file

    # Extract source IP from the 4th packet (index 3)
    if len(packets) >= 4 and packets[3].haslayer(IP):
        source_ip = packets[3][IP].src
        print(source_ip)

    # Extract destination IP from the 6th packet (index 5)
    if len(packets) >= 6 and packets[5].haslayer(IP):
        destination_ip = packets[5][IP].dst
        print(destination_ip)
    pass # print the source and destination ip addresses

show_source_destination_ip_address()

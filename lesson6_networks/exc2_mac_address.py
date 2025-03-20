from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
# from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_mac_address():
    packets = rdpcap(recording_path)
    third_packet = packets[2]
    
    if third_packet.haslayer(Ether):
        source_mac = third_packet[Ether].src
        print("Source MAC Address of 3rd Packet:", source_mac)
    else:
        print("No Ethernet layer found in the packet.")
    
    pass # print mac address

show_mac_address()

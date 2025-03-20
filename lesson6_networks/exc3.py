from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_username_password():
    packets = rdpcap(recording_path)  # Load the PCAP file

    for packet in packets:
        raw_data = packet[Raw].load.decode(errors="ignore")
        if 'username=' in raw_data:
            match = re.search(r'username=([^&]+)&password=([^&\s]+)', raw_data)
            username, password = match.groups()
            print(username, password)
            
show_username_password()
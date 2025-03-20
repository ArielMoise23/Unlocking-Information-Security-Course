from struct import *
packet = b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'

#### Don't change the code until this line ####

def show_details():
    # Unpack sender ID, receiver ID, and content size (little endian)
    sender_id, receiver_id, content_size = unpack('<III', packet[:12])


    # Extract the content (message text) safely
    message_text_bytes = packet[12:12+content_size-4]
    _, message_id = unpack('<II',message_text_bytes[:8])
    message_text_bytes = packet[20:12+content_size-4]

    # Ensure we decode only valid UTF-8 characters
    try:
        message_text = message_text_bytes.decode('utf-8')
    except UnicodeDecodeError:
        message_text = message_text_bytes.decode('utf-8', errors='ignore')  # Ignore invalid bytes

    # Extract session ID and checksum
    session_id, checksum = unpack('<II', packet[-8:])

    # Print required fields
    print("Sender ID:", sender_id)
    print("Message ID:", message_id)  # Assuming session ID is the message ID
    print("Message Text:", message_text)
    print("Checksum:", checksum)
    pass # print sender ID (decimal), message ID (decimal), the actual message (readable english text), and its checksum (decimal)

show_details()

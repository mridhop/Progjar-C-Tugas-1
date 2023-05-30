import sys
import socket
import logging

#set basic logging
logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    # ubah localhost jadi
    server_address = ('172.16.16.101', 32444)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # # Send data
    # message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    # logging.info(f"sending {message}")
    # sock.sendall(message.encode())
    # # Look for the response
    # amount_received = 0
    # amount_expected = len(message)
    # while amount_received < amount_expected:
    #     data = sock.recv(16)
    #     amount_received += len(data)
    #     logging.info(f"{data}")
    
    # Menerima data dari server
    logging.info('Receiving data from server...')
    while True:
        data = sock.recv(1024)
        logging.info(f"received {data}")
        if data:
            continue
        else:
            break
    logging.info('Received data from server.')
    
        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
    exit(0)
finally:
    logging.info("closing")
    sock.close()

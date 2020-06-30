import socket
import numpy as np
import time
UDP_IP = "192.168.1.83"
UDP_PORT = 5555

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(4096)
    data = data.decode('utf-8')
    data = data.split(',')
    data = np.array(data)
    data = data.astype(np.float)
    data = data[2:]
    print(data)
    #time.sleep(2)
    

import socket
UDP_IP = "192.168.1.83"
UDP_PORT = 5555

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(4096)
    print ("received message:", data)

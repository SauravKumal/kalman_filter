import socket
import numpy as np
import time
import collections
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

acceleration_data=collections.deque(100*[0],100)
interval = collections.deque(100*[0],100)

def getData():
    start_time = time.time()
    global acceleration_data
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
        acceleration_data.append(data[0])
        interval.append((time.time()-start_time)/1000)

getDataThread = threading.Thread(target = getData)
getDataThread.start()

style.use('seaborn-ticks')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    global acceleration_data
    global interval
    ax1.clear()
    ax1.plot(interval,acceleration_data)

anime = animation.FuncAnimation(fig,animate,interval=50)
plt.show()
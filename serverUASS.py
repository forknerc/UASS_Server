import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('',0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

broadcastPort = 8055
ctr = 0

while 1:
    data = "msg " + str(ctr)
    s.sendto(data, ('<broadcast>', broadcastPort))
    print "sent message: " + data
    time.sleep(2);
    ctr += 1

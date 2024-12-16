from ipaddress import *

net = ip_network('212.63.12.182/255.255.255.192', 0)

c = 0
for i in net:
    c += 1
    if str(i) == '212.63.12.182':
        print(c)
        break
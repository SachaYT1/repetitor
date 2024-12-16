from ipaddress import *

k=0

net = ip_network('172.16.168.0/255.255.248.0', False)

for ip in net:
    if format(ip, 'b').count('1')%5!=0:
        k += 1

print(k)
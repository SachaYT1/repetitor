from ipaddress import *

k = 0
ip1 = ip_network('192.168.240.0/255.255.255.0', 0)
for ip in ip1:
    print(ip)
    b = f'{ip:b}'

    b1 = bin(int(ip))[2:].zfill(32)
    if b.count('0') == b1.count('1'):
        k += 1

print(k)
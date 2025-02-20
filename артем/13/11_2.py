from ipaddress import *

net = ip_network(f'192.168.240.0/255.255.255.0', 0)
count = 0
for ip in net:
    ip2 = f'{ip:b}'
    if ip2.count('0') == ip2.count('1'):
        count += 1
print(count)
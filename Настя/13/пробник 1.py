from ipaddress import *

net = ip_network(f'10.112.0.0/255.248.0.0', 0)

count = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') % 3 == 0:
        count += 1

print(count)
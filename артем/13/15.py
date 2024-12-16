from ipaddress import *

net = ip_network(f'172.16.8.0/255.255.252.0',0)

print((net.num_addresses) // 33)

for i in net:
    print(i)
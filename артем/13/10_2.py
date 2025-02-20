from ipaddress import *

for i in range(32):
    net1 = ip_network(f'10.96.180.231/{i}', 0)
    net2 = ip_network(f'10.96.140.118/{i}', 0)
    if net1 != net2:
        print(32 - i)
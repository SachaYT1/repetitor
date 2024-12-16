from ipaddress import *

for i in range(33):
    net1 = ip_network(f'165.112.200.70/{i}', 0)
    net2 = ip_network(f'165.112.175.80/{i}', 0)
    if net1 == net2:
        print(net1.netmask, net1, i)
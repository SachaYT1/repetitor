from ipaddress import *

ip1 = ip_address('165.112.200.70')
ip2 = ip_address('165.112.175.80')

for i in range(33):
    net1 = ip_network(f'{ip1}/{i}', 0)
    net2 = ip_network(f'{ip2}/{i}', 0)
    if net1 == net2:
        print(net1, net1.netmask)
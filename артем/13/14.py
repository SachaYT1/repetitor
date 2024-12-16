from ipaddress import *

ip = ip_address('238.237.149.255')

for i in range(32):
    net = ip_network(f'238.237.149.255/{i}', 0)
    if str(net).startswith('238.237.148.0'):
        if net[0] < ip < net[-1]:
            print(net, net.netmask, net.broadcast_address)
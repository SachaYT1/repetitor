from ipaddress import *

for i in range(32):
    net = ip_network(f'191.173.145.240/{i}',0)
    if str(net).startswith('191.173.144.0'):
        print(net, net.netmask, net.num_addresses)

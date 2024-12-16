from ipaddress import *

for i in range(33):
    net = ip_network(f'158.116.11.146/{i}', 0)
    if str(net).startswith('158.116.0.0'):
        print(net, net.netmask)
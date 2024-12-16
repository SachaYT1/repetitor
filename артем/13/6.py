from ipaddress import *

for i in range(33):
    net = ip_network(f'173.103.25.118/{i}', 0)
    if str(net).startswith('173.103.24.0'):
        print(net, net.netmask)
        print(32 - i)

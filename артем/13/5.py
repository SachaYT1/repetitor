from ipaddress import *

for i in range(33):
    net = ip_network(f'122.21.49.91/{i}', 0)
    if str(net).startswith('122.21.48.0'):
        print(net, net.netmask)
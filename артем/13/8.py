from ipaddress import *

for i in range(33):
    net = ip_network(f'154.201.208.17/{i}', 0)
    if str(net).startswith('154.201.192.0'):
        print(net, net.netmask)
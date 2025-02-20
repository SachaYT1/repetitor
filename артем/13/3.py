from ipaddress import *


# цикл для перебора количества единиц (слева) для маски
for i in range(33):
    net = ip_network(f'118.193.30.139/{i}', 0)
    if str(net).startswith('118.193.24.0'):
        print(net, net.netmask)
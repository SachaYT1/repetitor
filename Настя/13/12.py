from ipaddress import *

net = ip_network('10.48.96.0/255.255.240.0', 0)

for i in net:

    s = ''.join(f'{x:>08b}' )
    print(i)

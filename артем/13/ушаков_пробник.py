from ipaddress import *
for i in range(20, 32):
    net = ip_network(f'192.168.32.160/{i}', 0)
    count = 0
    for ip in net:
        ip2 = f'{ip:b}'
        if ip2.count('1') % 4 == 0:
            count += 1
    if count == 120:
        print(i)

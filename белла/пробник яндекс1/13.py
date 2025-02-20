from ipaddress import *
ans = 0
for i in range(32):
    net1 = ip_network(f'61.58.73.42/{i}', 0)
    net2 = ip_network(f'61.58.75.136/{i}', 0)
    if net1 == net2 and i == 22:
        for ip in net1:
            ip2 = f'{ip:b}'
            if ip2.count('1') % 2 == 1:
                ans += 1
print(ans - 2)

from ipaddress import *
countMin = 10**6

for i in range(22, 32):
    count = 0
    net1 = ip_network(f'157.220.185.237/{i}', 0)
    net2 = ip_network(f'157.220.184.230/{i}', 0)
    if net1 == net2:
        for ip in net1:
            ip2 = f'{ip:b}'
            if ip2.count('1') == 15:
                count += 1
        countMin = min(count, countMin)

            
print(countMin)
    
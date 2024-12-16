from ipaddress import *

k = 0
net = ip_network(f'10.48.96.0/255.255.240.0', 0)
for i in net:
    # if format(i, 'b').count('1') > format(i, 'b').count('0'):
    #     k += 1

    b = f'{i:b}'
    #
    b1 = bin(int(i))[2:].zfill(32)
    if b.count('0') < b1.count('1'):
        k += 1

print(k)

from ipaddress import *




for a in range(0, 256):
    net = ip_network(f'192.214.{a}.184/255.255.255.224', 0)
    flag = True
    for ip in net:
        ip2 = f'{ip:b}'
        print(ip, ip2, sep=' ')
        if ip2.count('1') <= 15:
            flag = False
            break
    if flag:
        print(a)
        break
from models.models import IpPerfix
from modules.main import session

"""
private_ips

Class A:
10.0.0.0 to 10.255.255.255
Subnet Mask: 255.0.0.0

Class B:
172.16.0.0 to 172.31.255.255
Subnet Mask: 255.240.0.0

Class C:
192.168.0.0 to 192.168.255.255
Subnet Mask: 255.255.255.0

Loopback (127.0.0.0/8):
127.0.0.0 to 127.255.255.255
Subnet Mask: 255.0.0.0

"""

def create_private_prefixes():
    private_prefixes = ['192.168', '127.0']
    private_prefixes.extend([f'10.{i}' for i in range(256)])  # for '10.0' to '10.255'
    private_prefixes.extend([f'172.{i}' for i in range(16, 32)])  # for '172.16' to '172.31'
    private_prefixes.extend([f'0.{i}' for i in range(0, 256)]) # for '0.0' to '0.255'
    return private_prefixes



def add_ip_perfix():
    private_perfixes = create_private_prefixes()
    for x in range(256):
        for y in range(256):
            ip_perfix = f'{x}.{y}'
            if ip_perfix not in private_perfixes:
                ip_perfix_obj = IpPerfix(ip_perfix=ip_perfix)
                session.add(ip_perfix_obj)
            else:
                ip_perfix_obj = IpPerfix(ip_perfix=ip_perfix, is_public=False)
                session.add(ip_perfix_obj)

    session.commit()

if __name__ == '__main__':
    add_ip_perfix()
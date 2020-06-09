from sys import platform
import os
import subprocess
import socket

def GetIp(hostname = 'PI'):
    ips = GetNetworkIps()
    host = ""
    for x in ips:
        try:
            host = socket.gethostbyaddr(x)
            if host[0] == hostname:
                return x
        except OSError:
            continue

    return None

def GetNetworkIps():
    if platform == "win32":
        ips = subprocess.run(['arp', '-a'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
        toCheckIPs = []

        for x in ips:
            if x.strip().startswith('192.168.1'):
                toCheckIPs.append(x.strip().split(" ")[0])

        return toCheckIPs



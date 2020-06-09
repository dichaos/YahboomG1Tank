from sys import platform
import os
import subprocess

def GetIp(hostname = 'PI'):
    ips = GetNetworkIps()

    for x in ips:
        if platform == "win32":
            ping = subprocess.run(['ping', '-n', '1', '-a', x], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')[1].split(" ")[1]
            if ping == hostname:
                return x

    return None

def GetNetworkIps():
    if platform == "win32":
        ips = subprocess.run(['arp', '-a'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
        toCheckIPs = []

        for x in ips:
            if x.strip().startswith('192.168.1'):
                toCheckIPs.append(x.strip().split(" ")[0])

        return toCheckIPs



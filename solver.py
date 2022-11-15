import os
import pyperclip
import sys

os.system('cls')

soal_list = pyperclip.paste()
soal_list = soal_list.split('\n')

def getSubnetBlock(oktet, pref):
    host = 0

    if pref == 24:
        host = 256
    if pref == 25:
        host = 128
    if pref == 26:
        host = 64
    if pref == 27:
        host = 32
    if pref == 28:
        host = 16
    if pref == 29:
        host = 8
    if pref == 30:
        host = 4

    block = [0]
    previous_block = 0
    while int(oktet) not in range(previous_block, previous_block + host):
        block.append(previous_block + host)
        previous_block = previous_block + host

    print(block)
    print("Block per Subnet = " + str([previous_block, previous_block + host]))
    return [previous_block, previous_block + host]

if not sys.argv[1]:
    for soal in soal_list:
        prefix = int(soal.split('/')[1])
        ip = soal.split('/')[0]
        last_oktet = ip.split('.')[3]

        subnet_block = getSubnetBlock(last_oktet, prefix)
        networks = ip.split('.')
        networks.pop()
        network = ".".join(networks)
        print()
        print("IP Network = " + network + "." + str(subnet_block[0]))
        print("IP Awal = " + network + "." + str(subnet_block[0] + 1))
        print("IP Akhir = " + network + "." + str(subnet_block[1] - 2))
        print("IP Broadcast = " + network + "." + str(subnet_block[1] - 1))
        print()
        print("-------------------------------------------------------------------------")
        print()
else:
    soal = sys.argv[1]
    prefix = int(soal.split('/')[1])
    ip = soal.split('/')[0]
    last_oktet = ip.split('.')[3]

    subnet_block = getSubnetBlock(last_oktet, prefix)
    networks = ip.split('.')
    networks.pop()
    network = ".".join(networks)
    print()
    print("IP Network = " + network + "." + str(subnet_block[0]))
    print("IP Awal = " + network + "." + str(subnet_block[0] + 1))
    print("IP Akhir = " + network + "." + str(subnet_block[1] - 2))
    print("IP Broadcast = " + network + "." + str(subnet_block[1] - 1))
    print()
    print("-------------------------------------------------------------------------")
    print()
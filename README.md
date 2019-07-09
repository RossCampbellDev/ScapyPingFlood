usage: PingFlood.py [-h] [-t victim] [-n [numPings]] [-m [mask]]

Begin pinging random IP addresses, spoofing the source address to flood a
target with ICMP responses

optional arguments:
  -h, --help     show this help message and exit
  -t victim      the target IPv4 address
  -n [numPings]  the number of random addresses to send the spoofed pings to
  -m [mask]      subnet mask for addresses to ping


example:  ./PingFlood.py -t 192.168.0.1 -n 1000 -m 123.123.0.0/22
this will ping 192.168.0.1, spoofing the source addresses between 123.123.0.0 to 123.123.3.255 (i think? haha)

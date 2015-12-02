# -*- coding: utf-8 -*-

"""
Este fichero contiene la implementacion analizador de red que captura y recopila todas las peticiones DNS,
mostrandolas posteriormente por pantalla.
"""

from scapy.all import sniff, DNSQR


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
def filter_packet(x):
    x.show()

DNS_QUERIES = 0
DNS_DOMAINS = []


# ----------------------------------------------------------------------
def count_dns_request(pkt):
    global DNS_QUERIES

    if DNSQR in pkt:
        DNS_QUERIES += 1
        DNS_DOMAINS.append(pkt[DNSQR].qname)


def main():
    global DNS_QUERIES
    global DNS_DOMAINS

    print "[*] Ejecutando el sniffer"

    try:
        a = sniff(filter="udp and port 53", count=100, timeout=10, prn=count_dns_request)
    except KeyboardInterrupt:
        pass

    print "[*] Sniffer parado. Mostrando resultado obtenidos"

    print DNS_QUERIES
    print "[-] Dominios:"
    for x in DNS_DOMAINS:
        print x


if __name__ == '__main__':

    print banner()

    main()


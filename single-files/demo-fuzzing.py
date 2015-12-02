# -*- coding: utf-8 -*-

"""
Este fichero contiene la implementacion un fuzzer simple, usando paquetes ICMP
"""

import argparse

from scapy.all import IP, ICMP, sendp, RandInt, RandIP, RandShort, RandByte


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
def random_bool():
    return int(RandInt()) % 2


def main(args):
    print "[*] Comenzando el fuzzing..."

    pkt_lst = []

    for i in xrange(args.count):

        ip_layer = IP(dst=args.target)

        # Fuzz IP layer
        #
        #  Src ramdon?
        if random_bool():
            ip_layer.src = str(RandIP())
        # IP ID
        if random_bool():
            ip_layer.id = int(RandShort())
        # IP TTL
        if random_bool():
            ip_layer.ttl = int(RandInt()) % 255

        icmp_layer = ICMP()

        # Fuzz ICMP layer
        #
        #  Type random
        if random_bool():
            icmp_layer.type = int(RandByte())
        #  Seq random
        if random_bool():
            icmp_layer.seq = int(RandShort())

        pkt = ip_layer/icmp_layer

        pkt_lst.append(pkt)

    sendp(pkt_lst, inter=args.interval)

    print "[*] Enviado %s paquetes" % i


if __name__ == '__main__':

    print banner()

    args = argparse.ArgumentParser(description="Mini-fuzzer")
    args.add_argument("--target", dest="target", help="host destino", required=True)
    args.add_argument("-n", "--packet-count", dest="count", help="canitdad de paquetes a enviar",
                      type=int, default=5)
    args.add_argument("--interval", dest="interval", help="tiempo de envio entre paquetes",
                      type=float, default=0.2)
    parsed_args = args.parse_args()

    main(parsed_args)

# -*- coding: utf-8 -*-

"""
Este fichero contiene la implementacion de un escaner de puertos multi-hilo simple.
"""

import threading

from scapy.all import sr1, IP, TCP


CONCURRENCY = 5
OPEN_PORTS = []
VERBOSE = 1


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
def analyze_port(host, port, sem):
    print "[ii] Analizando el puerto %s" % port

    res = sr1(IP(dst=host)/TCP(dport=port), verbose=False, timeout=0.2)

    if res is not None and TCP in res:
        if res[TCP].flags == 18:
            OPEN_PORTS.append(port)

            print "Puerto %s abierto " % port

    sem.release()


# ----------------------------------------------------------------------
def main():
    sem = threading.BoundedSemaphore(value=CONCURRENCY)

    threads = []

    for x in xrange(78, 81):
        t = threading.Thread(target=analyze_port, args=("google.com", x, sem, ))
        threads.append(t)

        t.start()

        sem.acquire()

    for x in threads:
        x.join()

    print "[*] Puertos abiertos:"
    for x in OPEN_PORTS:
        print "     - %s/TCP" % x
    print

if __name__ == '__main__':

    print banner()

    main()

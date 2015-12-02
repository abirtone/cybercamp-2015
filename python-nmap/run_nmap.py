# -*- coding: utf-8 -*-

"""
Este fichero contiene la implementacion transformador de resultados de .XML de Nmap a JSON
"""

import six
import json
import nmap
import argparse


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
def main(args):

    print "[*] Preparing scan to %s" % args.target

    target = args.target
    ports = args.ports
    output = args.output

    # Prepare
    nm = nmap.PortScanner()
    nm.scan(hosts=target, ports=ports)

    # Command info
    print "[*] I Will launch this command: %s" % nm.command_line()
    nm.scan(args.target, args.ports)

    # Launch
    results = {}
    for x in nm.csv().split("\n")[1:-1]:
        splited_line = x.split(";")

        host = splited_line[0]
        proto = splited_line[1]
        port = splited_line[2]
        state = splited_line[4]

        try:
            if state == "open":
                results[host].append({proto: port})
        except KeyError:
            results[host] = []
            results[host].append({proto: port})

    # Store info
    file_info = output or "scan_%s.json" % target
    with open(file_info, "w") as f:
        json.dump(results, f)

    print "[*] File '%s' was generated with results" % file_info

if __name__ == '__main__':

    six.print_(banner())

    examples = '''
Usage:
    %(tool)s 192.168.1.1
    ''' % dict(tool="nmap2json")

    parser = argparse.ArgumentParser(description='Nmap to JSON', epilog=examples,  # TODO
                                     formatter_class=argparse.RawTextHelpFormatter)

    # Main options
    parser.add_argument("-t", dest="target", help="target IP", required=True)
    parser.add_argument("-p", dest="ports", help="comma separated ports", default="80,8080,90")
    parser.add_argument("-o", dest="output", help="output json file with extention.", default=None)

    parsed_args = parser.parse_args()

    main(parsed_args)

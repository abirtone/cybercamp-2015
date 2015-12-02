# -*- coding: utf-8 -*-

import six
import argparse
import logging

log = logging.getLogger(__name__)


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

    from .api import run_console, GlobalParameters

    six.print_(banner())

    examples = '''
Examples:

    * Scan a target:
        %(tool_name)s TARGET

    * Scan with port range: 80-1024:
        %(tool_name)s TARGET -p1 80 -p2 1024
    '''  % dict(tool_name="cyberscan")

    parser = argparse.ArgumentParser(description='%s port scanner' % "cyberscan".capitalize(), epilog=examples,
                                     formatter_class=argparse.RawTextHelpFormatter)

    # Main options
    parser.add_argument("target", metavar="TARGET", nargs="*")
    parser.add_argument("-v", "--verbosity", dest="verbose", action="count", help="verbosity level: -v, -vv, -vvv.", default=0)
    parser.add_argument("-p1", "--port-init", dest="port_ini", help="verbosity level: -v, -vv, -vvv.")
    parser.add_argument("-p2", "--port-end", dest="port_end", help="verbosity level: -v, -vv, -vvv.")

    parsed_args = parser.parse_args()

    # Set Global Config
    config = GlobalParameters(parsed_args)

    run_console(config)

if __name__ == "__main__" and __package__ is None:
    # --------------------------------------------------------------------------
    #
    # INTERNAL USE: DO NOT MODIFY THIS SECTION!!!!!
    #
    # --------------------------------------------------------------------------
    import sys
    import os
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(1, parent_dir)
    import cyberscan_lib
    __package__ = str("cyberscan_lib")

    del sys, os

    main()

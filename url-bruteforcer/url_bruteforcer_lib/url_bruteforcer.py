# -*- coding: utf-8 -*-

import six
import argparse
import logging

logging.basicConfig(format="%(message)s")
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

    - Looking for urls in target
        %(tool_name)s -w cms/drupal_plugins TARGET

    - Looking for urls in target with error rate page comparison of 80 percent:
        %(tool_name)s -w login-file-locations/Logins -r 80 TARGET

    ** Target must be as format: http://target.com
    *** Wordlist list are under directory: resources/fuzzdb-master/discovery/predictable-filepaths/
    **** You DON'T need to specify absolute path to wordlist. Correct format is: login-file-locations/Logins
    ''' % dict(tool_name="url_bruteforcer")

    parser = argparse.ArgumentParser(description='%s: simple, but smart, URL bruteforcer' % "url_bruteforcer".capitalize(), epilog=examples,
                                     formatter_class=argparse.RawTextHelpFormatter)

    # Main options
    parser.add_argument("target", metavar="TARGET", nargs="*")
    parser.add_argument("-v", "--verbosity", dest="verbose", action="count", help="verbosity level: -v, -vv, -vvv.",
                        default=1)
    parser.add_argument("-w", "--wordlist", dest="wordlist", help="wordlist to use", required=True)
    parser.add_argument("-r", "--ratio", dest="ratio", help="matching error value. 0-100.", type=int, default=60)
    parser.add_argument("-s", "--smart", dest="smart", help="enable smart mode", type=bool, default=True)

    parsed_args = parser.parse_args()

    # Check targets
    if not parsed_args.target:
        six.print_("[!] At least 1 target must be specified.")
        exit(1)

    # Setting log level
    log.setLevel(abs(50 - (parsed_args.verbose * 10)))

    # Set Global Config
    config = GlobalParameters(parsed_args)

    try:
        run_console(config)
    except KeyboardInterrupt:
        log.warning("[*] CTRL+C caught. Exiting...")
    except Exception as e:
        log.critical("[!] Unhandled exception: %s" % str(e))

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
    import url_bruteforcer_lib
    __package__ = str("url_bruteforcer_lib")
    # Checks Python version
    if sys.version_info < 3:
        print("\n[!] You need a Python version greater than 3.x\n")
        exit(1)

    del sys, os

    main()

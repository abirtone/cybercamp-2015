# -*- coding: utf-8 -*-

"""
This file contains API calls and Data
"""

import six

from sys import version_info
from termcolor import colored

from .data import *
from .libs.fuzz_utils import fuzz

__version__ = "1.0.0"
__all__ = ["run_console", "run", "GlobalParameters"]


# --------------------------------------------------------------------------
#
# Command line options
#
# --------------------------------------------------------------------------
def run_console(config):
    """
    :param config: GlobalParameters option instance
    :type config: `GlobalParameters`

    :raises: TypeError
    """
    if not isinstance(config, GlobalParameters):
        raise TypeError("Expected GlobalParameters, got '%s' instead" % type(config))

    six.print_(colored("[*]", "blue"), "Starting url_bruteforcer execution")
    r = run(config)

    # Show results
    if r:
        six.print_("[*] Discovered URLs:")

    for x in r:
        six.print_("    - %s" % x)

    six.print_(colored("[*]", "blue"), "Done!")


# ----------------------------------------------------------------------
#
# API call
#
# ----------------------------------------------------------------------
def run(config):
    """
    :param config: GlobalParameters option instance
    :type config: `GlobalParameters`

    :raises: TypeError
    """
    if not isinstance(config, GlobalParameters):
        raise TypeError("Expected GlobalParameters, got '%s' instead" % type(config))
    # --------------------------------------------------------------------------
    # Checks Python version
    # --------------------------------------------------------------------------
    if version_info < 3:
        raise RuntimeError("You need Python 3.x or higher to run url_bruteforcer")

    return fuzz(config)

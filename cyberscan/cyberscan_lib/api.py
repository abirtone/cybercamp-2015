# -*- coding: utf-8 -*-

"""
This file contains API calls and Data
"""

import six

from sys import version_info
# from termcolor import colored

from .data import *
from .libs.scanner import analyze_port

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

    six.print_("[*] Starting cyberscan execution")
    b = run(config)

    for x in b:
        six.print_("   - port %s/TCP" % x)
    six.print_("[*] Done!")


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

    results = []

    for x in range(int(config.port_ini), int(config.port_end)):
        if analyze_port(config.target[0], x):
            results.append(x)

    return results

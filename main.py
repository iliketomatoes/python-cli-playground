#!/usr/bin/env python3
"""
Entry module of the app
"""

from exercises import module_one

__author__ = "Giancarlo Soverini"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """

    # Print Panda version
    module_one.printVersion()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

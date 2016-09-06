#!/usr/bin/env python

import time
import sys

if __name__ == '__main__':
    print """This is just a script that prints a dot every second to the console
    until its killed"""
    while True:
        time.sleep(1)
        print '.',
        sys.stdout.flush()

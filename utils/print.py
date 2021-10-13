""" Developing functions to enabled or disabled print """

import os
import sys

# Disable print
def disablePrint():
    sys.stdout = open(os.devnull, 'w')

# Enable print
def enablePrint():
    sys.stdout = sys.__stdout__
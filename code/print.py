import sys, os

# Disable print
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Enable print
def enablePrint():
    sys.stdout = sys.__stdout__

print('This will print')

blockPrint()
print("This won't")

enablePrint()
print("This will too")
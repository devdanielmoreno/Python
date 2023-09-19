# arg00b.py
import sys

print("Arguments: %d"%(len(sys.argv)))
if sys.argv[3] == 'a':
   print("Suma")
else:
   print("Multiplico")
print("Argument 1: %d"%int(sys.argv[1]))
print("Argument 2: %.2f"%float(sys.argv[2]))
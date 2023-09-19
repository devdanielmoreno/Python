# arg00.py
import sys

print("Arguments: %d"%(len(sys.argv)))
i = 0
for arg in sys.argv:
   print("argv[%d]: %s"%(i,arg))
   i += 1
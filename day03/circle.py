import sys
import math
if len(sys.argv) != 2:
  sys.exit("Needs one argument: radius")
rad = float(sys.argv[1])
area = math.pi * rad**2
cir = 2 * math.pi * rad
print("The area is:", area)
print("The circumference is:", cir)

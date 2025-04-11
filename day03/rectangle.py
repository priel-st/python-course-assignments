import sys
import math
if len(sys.argv) != 3:
  sys.exit("Needs two arguments: height width")
height = float(sys.argv[1])
width = float(sys.argv[2])
area = height * width
perimeter = 2*(height+width)
print("The area is:", area)
print("The perimeter is:", perimeter)

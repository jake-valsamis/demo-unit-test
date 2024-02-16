import sys
from circles import circle_area

if (len(sys.argv) >= 1):
    radius = int(sys.argv[1])
else:
    radius = 5

circle_area = circle_area(radius)
print(f"A circle with a radius of {radius} has an area of {circle_area}")
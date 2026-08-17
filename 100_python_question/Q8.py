#8. Write a program to find the euclidean distance between two coordinates.

# Eucliden distance is the distance between two coordinate point
# 2D space: (d = sqrt{(x2 - x1)^2 + (y2 - y1)^2})
# 3D space: (d = sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2})
import math
x1=int(input("Enter x1 : "))
x2=int(input("Enter x2 : "))
y1=int(input("Enter y1 : "))
y2=int(input("Enter y2 : "))

# to do square root = import math
                    # math.sqrt()
# for power we can use pow() or **
distance=math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
print(distance)
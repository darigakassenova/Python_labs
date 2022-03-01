from math import pi, tan
def area(num, len):
    area = (num*pow(len,2))/(4*tan(pi/num))
    return area

num, len = int(input()), float(input())
print(area(num, len))


from math import pi
def degree_to_radian(d):
    r = (d*pi)/180
    return r

d = int(input())
print(degree_to_radian(d))
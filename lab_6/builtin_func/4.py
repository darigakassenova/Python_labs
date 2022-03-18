import time 
import math
num = int(input())
sec = int(input())
print("Square root of" , num, "after", end=" ")
time.sleep(sec/1000)
print(sec, "miliseconds is", math.sqrt(num))
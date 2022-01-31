m = int(input())
n = input()
if n=='b':
    print(m*1024)
else:
    x = int(input())
    y = m/1024
    print(round(y,x))
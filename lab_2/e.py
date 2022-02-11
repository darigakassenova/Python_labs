s = input().split()
if len(s) == 2:
    n = int(s[0])
    x = int(s[1])
if len(s) == 1:
    n = int(s[0])
    x = int(input())
a = []
for i in range(n):
    a.append(x+2*i)
res = a[0]
for i in range(1,n):
    res = int(res)^int(a[i])
print(res)

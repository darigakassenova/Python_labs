a = {}
for i in range(int(input())):
    n, m = map(str,input().split())
    if n not in a:
        a[n]=int(m)
    else:
        a[n]+=int(m)
b = []
for i in a.values():
    b.append(i)
b.sort()
for i in sorted(a):
    if a[i] == b[-1]:
        print(i,'is lucky!')
    else:
        print(i,'has to receive',b[-1]-a[i],'tenge')
    
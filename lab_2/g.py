d = {}
cnt = 0
for i in range(int(input())):
    n, w = input().split()
    if w not in d:
        d[w] = 1
        cnt+=1
    else:
        d[w]+=1
        cnt+=1

h = {}
for i in range(int(input())):
    n, p, c = input().split()
    cnt1 = int(c)
    if p in d and d[p]<=cnt1:
        cnt-=d[p]
        d.pop(p)
    if p in d and d[p]>cnt1:
        cnt-=cnt1
        d[p]-=cnt1

print("Demons left:", cnt)
cr = []
t  = []
for i in range(int(input())):
    name = input().split()
    if name[0]=="1":
        cr.append(name[1])
    else:
        t.append(cr[0])
        del cr[0]
for i in t:
    print(i, end=" ")
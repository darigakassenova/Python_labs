def num(p):
    cnt = 0
    for i in range(len(p)):
        if "0"<=p[i]<="9":
            cnt+=1
    if cnt>=1:
       return True

n = set()
for i in range(int(input())):
    p = input()
    if p!=p.lower() and p!=p.upper() and num(p)==True:
        n.add(p)

print(len(n))
print("\n".join(sorted(n)))
    
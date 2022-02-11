a = []
while True:
    n = int(input())
    if n==0:
        break
    a.append(n)
b = a[::-1]
for i in range(len(a)//2):
    print(a[i]+b[i], end=" ")
            
if len(a)%2!=0:
    print(a[len(a)//2])

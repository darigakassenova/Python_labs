n, f = map(int, input().split())
k = 0
for i in range(2, n):
    if(n%i==0):
        k+=1
if(k==0 and n<=500 and f%2==0):
    print("Good job!")
else:
    print("Try next time!")

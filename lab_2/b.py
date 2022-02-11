a = int(input())
n = []
for i in input().split():
    n.append(int(i))  
n.sort()
print(n[-1]*n[-2])

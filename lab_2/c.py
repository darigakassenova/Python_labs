n = int(input())
cnt = 0
cnt1 = 0
for i in range(n):
    for j in range(n):
        if(i == j):
            print(i*j, end=" ")
        elif i==0:
            print(cnt, end=" ")
        elif j==0:
            print(cnt1, end=" ")
        else:
            print(0, end=" ")
        cnt+=1
    print()
    cnt1+=1
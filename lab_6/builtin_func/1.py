def mult(n):
    m = 1
    for i in n:
        m*=int(i)
    return m
list = []
for i in input().split():
    list.append(i)
print(mult(list))
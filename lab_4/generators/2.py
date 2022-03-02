def even(n):
    for i in range(0, n):
        if i%2==0:
            yield i

n = int(input())
a = []
for i in even(n):
    a.append(str(i))

print(",".join(a))
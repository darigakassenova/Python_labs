def square(n):
    for i in range(n):
        yield i**2

n = int(input())
for i in square(n):
    print(i)
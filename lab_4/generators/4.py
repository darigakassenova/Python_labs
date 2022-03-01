def squares(a, b):
    for i in range(a, b):
        yield i**2

a, b = int(input()), int(input())
for i in squares(a, b):
    print(i)
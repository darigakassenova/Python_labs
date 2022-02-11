x, y = input().split()
x = int(x)
y = int(y)
arr = []
for i in range(int(input())):
    coordinate = input()
    x1, y1 = coordinate.split()
    x1 = int(x1)
    y1 = int(y1)
    distance = ((x1-x)**2+(y1-y)**2)**(0.5)
    arr.append((coordinate,distance))
arr.sort(key = lambda x:x[1])
for i in arr:
    print(i[0])
def has_33(a):
    for i in range(len(a)):
        if a[i:i+2] == [3,3]:
            return True
    return False

list = []
for i in input().split():
    list.append(int(i))
print(has_33(list))

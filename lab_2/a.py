def reach(arr):
    ind = 0
    max = 0
    while ind<len(arr):
        if ind>max:
            return False
        if ind+arr[ind]>max:
            max = ind+arr[ind]
        if max>=len(arr)-1:
            return  True
        ind+=1

arr = list(map(int, input().split()))
if reach(arr):
    print(1)
else:
    print(0)
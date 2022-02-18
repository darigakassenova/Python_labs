def spy_game(nums):
    cnt = 0
    for i in nums:
        if i==0 and cnt==0:
            cnt += 1
        if i==0 and cnt>0:
            cnt += 1
        if i==7 and cnt>1:
            return True
    return False

list = []
for i in input().split():
    list.append(int(i))
print(spy_game(list))

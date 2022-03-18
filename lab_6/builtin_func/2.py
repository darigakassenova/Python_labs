word = input()
cnt = 0
for i in word:
    if i.islower():
        cnt+=1
print("lower case letters:", cnt)

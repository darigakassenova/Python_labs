s = str(input())
sum=0
for i in range(len(s)):
    x=ord(s[i])
    sum+=x
if(sum>300):
    print("It is tasty!")
else:
    print("Oh, no!")
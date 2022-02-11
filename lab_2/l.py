brack = input()
left = ["(" , "{", "["]
a = []
cnt = 0
for i in range(len(brack)):
    if brack[i] in left:
        a.append(brack[i])
    else:
        if len(a)==0:
            cnt+=1
            break
        else:
            if brack[i]==")" and a[-1]!="(":
                cnt+=1
                break
            if brack[i]=="}" and a[-1]!="{":
                cnt+=1
                break
            if brack[i]=="]" and a[-1]!="[":
                cnt+=1
                break
        a.pop(-1)   
if cnt>0 or len(a)>0:
    print("No")
else:
    print("Yes")
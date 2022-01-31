n=int(input())
login = []
num = []
t = "@gmail.com"
for i in range(0,n):
    s = str(input())
    login.append(s)
for i in login:
    if(t in i):
        num.append(i)
for i in num:
    i.replace("@gmail.com" , " ")
for i in num:
    print(i[:i.index(t)])

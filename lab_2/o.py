def str_(s):
    if s=="ONE":
        return 1
    if s=="TWO":
        return 2
    if s=="THR":
        return 3
    if s=="FOU":
        return 4
    if s=="FIV":
        return 5
    if s=="SIX":
        return 6
    if s=="SEV":
        return 7
    if s=="EIG":
        return 8
    if s=="NIN":
        return 9
    if s=="ZER":
        return 0
def num_(n):
    if n=="9":
        return "NIN"
    if n=="8":
        return "EIG"
    if n=="7":
        return "SEV"
    if n=="6":
        return "SIX"
    if n=="5":
        return "FIV"
    if n=="4":
        return "FOU"
    if n=="3":
        return "THR"
    if n=="2":
        return "TWO"
    if n=="1":
        return "ONE"
    if n=="0":
        return "ZER"

def res(m):
    cnt = 0
    for i in m:
        cnt = (cnt + str_(i)) * 10
    return int(cnt/10)

a = input()
arr = []
arr1 = []
word = ""
for i in range(a.find("+")):
    word+=a[i]
    if (i+1)%3==0:
        arr.append(word)
        #print(word)
        word = ""

for i in range(a.find("+")+1, len(a)):
    word+=a[i]
    if i%3==0:
        arr1.append(word)
        #print(word)
        word = ""

result = str(res(arr) + res(arr1))
for i in result:
    print(num_(i), end="") 


    #arr.sort(key = lambda x:x[1])
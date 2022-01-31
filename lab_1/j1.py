s = str(input())
sen = s.split()
for i in range(len(sen)):
    if(len(sen[i])>=3):
        print(sen[i], end=" ")
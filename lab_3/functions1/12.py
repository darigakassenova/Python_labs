def histogram(list):
    for i in list:
        print('*'*i)

list = []
for i in input().split():
    list.append(int(i))  
print(histogram(list)) 
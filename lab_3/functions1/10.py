def unique_list(list):
  x = []
  for i in list:
    if i not in x:
      x.append(i)
  return x

list = []
for i in input().split():
    list.append(int(i))  
print(unique_list(list)) 
import re
txt = input()
x = re.findall('[A-Z]+[a-z]+$', txt)
if x:
    print("Yes!")
else:
    print("No!")

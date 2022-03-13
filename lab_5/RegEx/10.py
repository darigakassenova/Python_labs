import re
txt = input()
x = re.sub(r'(?<!^)(?=[A-Z])', '_', txt).lower()
print(x) 
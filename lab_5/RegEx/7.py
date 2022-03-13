import re
def camel(m):
    return m.group(1).upper()
txt = input()
x = re.sub(r"_(\w)", camel, txt)
print(x)

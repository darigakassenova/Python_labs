n = input()
p = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
n1 = ""
for i in n:
    if i not in p:
        n1+=i
s = {s1 for s1 in n1.split(" ")}

print(len(s))
print("\n".join(sorted(s)))

f = open("test.txt")
f1 = open("test2.txt", "w")
for line in f:
    f1.write(line)
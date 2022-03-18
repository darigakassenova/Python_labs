file = open("test.txt", "r")
cnt = 0
f = file.read()
for i in f.split("\n"):
	cnt += 1		
print("number of lines in the file:", cnt-1)

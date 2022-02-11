dates = []
while True:
    s = input()
    if s=="0":
        break
    dd, mm, yy = s.split(" ")
    arr = [yy, mm, dd]
    dates.append(arr)
dates.sort()
for i in range(len(dates)):
    print(*dates[i][::-1])
    
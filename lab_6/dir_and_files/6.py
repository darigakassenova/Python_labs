for i in range(0, 26):
    upper_case = chr(65+i)
    f = open(upper_case + ".txt", "w")
    f.writelines(upper_case)

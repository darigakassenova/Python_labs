import os
file = '/Users/dariga/Desktop/PP2/lab_6/dir_and_files/test3.txt'
if os.path.exists(file):
    os.remove(file)
else:
    print("file doesn't exists")
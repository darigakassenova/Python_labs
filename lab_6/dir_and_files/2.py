import os
print('Exist:', os.access('c:/Users/dariga/Desktop/PP2/lab_6', os.F_OK))
print('Readable:', os.access('c:/Users/dariga/Desktop/PP2/lab_6', os.R_OK))
print('Writable:', os.access('c:/Users/dariga/Desktop/PP2/lab_6', os.W_OK))
print('Executable:', os.access('c:/Users/dariga/Desktop/PP2/lab_6', os.X_OK))

import os
WORKING_DIR = os.getcwd()
for root, dirs, files in os.walk(WORKING_DIR):
  print(root)
  print(f'dirs: {dirs}')
  print(f'files: {files}')
  print('----------------')
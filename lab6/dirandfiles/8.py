import os

path = r'delfile.txt'
if os.path.exists(path):
   os.remove(path)
   print('removed')
else:
   print('your file does not exists')
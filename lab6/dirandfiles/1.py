import os

for i in os.listdir(r'/Users/nurasylnurtaza/Desktop/pp2-22B030569'):
    if os.path.isdir(r'/Users/nurasylnurtaza/Desktop/pp2-22B030569'):
        print(i, end = ' ')
for i in os.listdir(r'/Users/nurasylnurtaza/Desktop/pp2-22B030569'):
    if os.path.isfile(r'/Users/nurasylnurtaza/Desktop/pp2-22B030569'):
        print(i, end = ' ')
for i in os.listdir(r'/Users/nurasylnurtaza/Desktop/pp2-22B030569'):
   print(i)
file = open('realmadrid.txt', 'w')
mylist = ['Real Madrid the best team in history', 'i am Nurasyl', 1, 115]
for i in mylist:
    file.write(str(i) + '\n')
file.close()
f = open('realmadrid.txt', 'r')
print(f.read())
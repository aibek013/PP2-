file1 = open('realmadrid.txt', 'r')
file2 = open('text.txt', 'w')

for i in file1:
    file2.write(str(i))
file1.close()
file2.close()

file2 = open('text.txt', 'r')
print(file2.read())
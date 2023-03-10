file = open('realmadrid.txt', 'r')

count = 0
for i in file:
    if i != '\n':
        count += 1
print(count)
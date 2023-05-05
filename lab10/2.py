import csv, psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5432,
    user='postgres',
    password='qwerty123'
)

current = config.cursor()
arr = []

sql1 = '''
    INSERT INTO phonebook
    VALUES (%s, %s, %s, %s);
'''


with open('pb.csv') as f:
    reader = csv.reader(f, delimiter=',')
        
    for row in reader:
        row[0] = int(row[0])
        arr.append(row)
for row in arr:
    current.execute(sql1, row)    

current.close()
config.commit()
config.close()
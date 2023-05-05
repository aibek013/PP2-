import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5432,
    user='postgres',
    password='qwerty123'
)

current = config.cursor()
1
sql1 = '''
    INSERT INTO phonebook
    VALUES (%s, %s, %s, %s);
'''
print("ID: ")
id = input()
print("Name:")
name = input()
print("Relationship")
rel = input()
print("Phone number:")
number = input()
current.execute(sql1, (id, name, rel, number))

current.close()
config.commit()
config.close()
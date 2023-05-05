import psycopg2
config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'qwerty123'
)

current = config.cursor()
sql1 = """
    SELECT name FROM phonebook WHERE relationship= 'CR7' ;
"""

current.execute(sql1)
rel = current.fetchall()
print(rel)
current.close()
config.commit()
config.close()
import psycopg2
config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'qwerty123'
)

current = config.cursor()
sql1 = """
    CREATE TABLE phonebook(
        id INTEGER,
        name TEXT,
        relationship TEXT,
        phone_number VARCHAR(25)
    );
"""

current.execute(sql1)
current.close()
config.commit()
config.close()
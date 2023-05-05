import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    port=5432,
    user='postgres',
    password='qwerty123'
)

current = config.cursor()

try:
    user_id = input("Enter ID: ")
    sql = '''
            DELETE FROM phonebook WHERE id = %s;
        '''
    current.execute(sql, ( user_id))
    config.commit()
except:
    print("ERROR!!!!")

current.close()
config.close()
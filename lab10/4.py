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
    to_change = input("What do you want to change?: ")
    data = input("To what data set the old data?: ")
    to_change = to_change.lower()
    if to_change == 'name':
        sql1 = '''
            UPDATE phonebook SET name = %s WHERE id = %s;
        '''
    elif to_change == 'phone_number':
        sql1 = '''
            UPDATE phonebook SET phone_number = %s WHERE id = %s;
        '''
    current.execute(sql1, ( data, user_id))
    config.commit()
except:
    print("ERROR!!")

current.close()
config.close()
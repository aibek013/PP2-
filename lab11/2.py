import psycopg2

namee = input('Enter name you want insert...\n')
phonee = input('Enter phone you want insert...\n')

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = 'qwertysd'
)
cur = conn.cursor()

# procedure was created inside pg admin/tools/query tool
'''
create or replace procedure insert_new_user(namee varchar(255), phonee varchar(255))
as 
$$
begin
    insert into PhoneBook(name, phone) values ($1, $2);
end;
$$ language plpgsql;
'''
cur.execute(f'CALL insert_new_user(\'{namee}\', \'{phonee}\')')


cur.close()
conn.commit()
conn.close()
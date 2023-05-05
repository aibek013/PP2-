sql = '''
CREATE TABLE  if not exists students (
    id serial NOT NULL,
    name VARCHAR(255) ,
    age integer
);
'''

import psycopg2, random


conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = 'qwertysd'
)

cur = conn.cursor()

sts = [
  f'({i}, \'{f"student{i}"}\', {random.randint(12, 19)})'
  for i in range(1000)
]
insert_sql = f"insert into students (id, name, age) values {', '.join(sts)};"
# cur.execute(insert_sql)


page_current = 2
records_per_page = 10  # resulting "LIMIT" part of query: "LIMIT 10"   there we can take any number we want
offset = (page_current - 1) * records_per_page # resulting "OFFSET" part of query: "OFFSET 10"

s = "SELECT * FROM students ORDER BY id  LIMIT "
s +=  str(records_per_page)
s += " OFFSET " + str(offset)


cur.execute(s)
res = cur.fetchall()
print(res)


cur.close()
conn.commit()
conn.close()
import sqlite3

conn=sqlite3.connect(r'mydb1.db')
cursor=conn.cursor()

# conn.execute("drop table puzzle;")
# conn.execute("drop table credentials;")

cursor.execute('''create table puzzle
                (p_no int primary key,
                easy char(1),
                medium char(1),
                hard char(1),
                expert char(1),
                Unsolved char(10));''')


cursor.execute('''create table credentials
             (user_name char(50) primary key,
             password int not null,
             recently_played int,
             foreign key(recently_played) references puzzle(p_no) );''')

cursor.execute("insert into credentials values('arun2110763@ssn.edu.in','a',1);")
cursor.execute("insert into credentials values('ashwin2110586@ssn.edu.in','b',101);")
cursor.execute("insert into credentials values('badri2110867@ssn.edu.in','c',201);")
cursor.execute("insert into credentials values('arshat2110684@ssn.edu.in','d',301);")
cursor.execute("insert into credentials values('arunasree2110371@ssn.edu.in','e',302);")
cursor.execute("insert into credentials values('arjun2111023@ssn.edu.in','f',303);")

values1=[]
for i in range(1,101):
    values1.append([i,'T','F','F','F','e'+str(i)])

for i in range(101,201):
    values1.append([i,'F','T','F','F','m'+str(i)])

for i in range(201,301):
    values1.append([i,'F','F','T','F','h'+str(i)])

for i in range(301,401):
    values1.append([i,'F','F','F','T','ex'+str(i)])

query = 'INSERT INTO puzzle VALUES(?,?,?,?,?,?);'
# Replace 'your_table_name' with the actual table name and specify the columns

# Split the values into chunks of 100
chunks = [values1[i:i+100] for i in range(0, len(values1), 100)]

# Iterate over each chunk and execute the INSERT statement
for chunk in chunks:
    cursor.executemany(query, chunk)

# Commit the changes and close the connection
conn.commit()
conn.close()
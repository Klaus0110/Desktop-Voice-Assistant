import sqlite3

conn = sqlite3.connect("contacts.db")
print("Opened database successfully")

conn.execute('''CREATE TABLE CONTACTS
    (SNO INT PRIMARY KEY NOT NULL,
    UNAME TEXT NOT NULL,
    EMAIL CHAR NOT NULL,
    PASSWORD CHAR)''')

print("Table created successfully")

conn.execute("INSERT INTO CONTACTS (SNO, UNAME, EMAIL, PASSWORD) \
    VALUES (1, 'KUSH', 'kingkc0110@gmail.com', '********')")

conn.execute("INSERT INTO CONTACTS (SNO, UNAME, EMAIL) \
    VALUES (2, 'ME', 'vskushagra@outlook.com')")

conn.commit()
print("Records created sucessfully")
conn.close()

conn.close()

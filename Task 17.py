Task 17

• Create a connection for DB and print the version using a python program
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)
print(mydb)
import sys
cur = mydb.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("DBMS Version :",str(data))

#-----------------------------------------------------------------------------
 Create a multiple tables & insert data in table
dbse = mydb.cursor()
dbse.execute("CREATE DATABASE mydatabase")
dbse = mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
  print(entry)

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="mydatabase"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE customers (Employee_name VARCHAR(255), Employee_dep VARCHAR(255), Employee_id VARCHAR(255))")
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Office (emp_name VARCHAR(255), Employee_id VARCHAR(255) ,EMP_ADDRESS VARCHAR(255))")
dbse =mydb.cursor()
dbse.execute("CREATE TABLE Student(rollno INT(24) , STUD_NAME VARCHAR(255) , MARK INT(3))")
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
#-----------------------------------------------------------------------------------
   Create a employee table and read all the employee name in the table using for loop

 mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Employee1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="mydatabase"
)
mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"
val = ("123","shef","SahakarNagar 56")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"
val = ("124","Rani","T Nagar 58")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"
val = ("125","Raju","ravivar peth 58")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id,name, address) VALUES (%s,%s,%s)"
val = [
  ('1','Paul', 'Lowstreet 4'),
  ('2','Arana', 'Apple st 652'),
  ('3','Harshad', 'Mountain 21'),
  ('4','Mishal', 'Valley 345'),
  ('5','Saurabh', 'Ocean blvd 2'),
  ('6','Vishal', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "was inserted.")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Employee1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM Employee1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
 

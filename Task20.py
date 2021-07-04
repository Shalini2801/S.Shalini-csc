import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="8639488740",
    database="mysql"
)
cur = conn.cursor()
# cur.execute("CREATE TABLE employee(firstname VARCHAR(255),id INT,salary FLOAT)")
# cur.execute("SHOW TABLES")
# for i in cur:
#     print(i)
sql =("INSERT INTO employee(firstname,id,salary)VALUES(%s,%s,%s)")
values = [("manee","101","30000"),
          ("ramesh","102","25000"),
          ("suresh","103","20000"),
          ("rahul","104","30000")]
cur.executemany(sql,values)
conn.commit()
#a)writing a query to get max and min salary from employee table
cur.execute("SELECT MIN(salary),MAX(salary) FROM employee")
myresult = cur.fetchall()
for i in myresult:
    print(i)
#b)number of employees working
cur.execute("SELECT COUNT(DISTINCT firstname) FROM employee")
result = cur.fetchall()
for i in result:
    print(i)
#c)to get first 3 characters of fistname from employee table
cur.execute("SELECT DISTINCT SUBSTRING(firstname,1,3) FROM employee")
res = cur.fetchall()
for i in res:
    print(i)
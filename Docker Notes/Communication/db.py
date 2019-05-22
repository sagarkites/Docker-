import pymysql

# Open database connection
db = pymysql.connect("mysql-server","root","sagar215","mysql" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)
FIRST_NAME = "sagar"
LAST_NAME = "scott"
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME) VALUES ('%s', '%s')" % (FIRST_NAME, LAST_NAME))
db.commit()
cursor.execute("SELECT * FROM EMPLOYEE")
result = cursor.fetchall()
print result
# disconnect from server
db.close()

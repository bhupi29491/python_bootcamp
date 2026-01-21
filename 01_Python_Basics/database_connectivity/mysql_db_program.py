import pymysql

try:
    connectionObject = pymysql.connect(
        user="root",
        password="root",
        host="localhost",
        port=3309
    )

    cursorObject = connectionObject.cursor()
    print(cursorObject)

    # step4: Create the required SQL Query
    sql = "SHOW DATABASES;"

    # step5: Execute the required SQL query by using execute() method of cursorObject
    count = cursorObject.execute(sql)
    print(count)

except pymysql.MySQLError as e:
    print("MySQL Error:", e)

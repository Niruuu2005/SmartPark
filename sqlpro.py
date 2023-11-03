import mysql.connector

a=mysql.connector.connect(host="localhost",user="root",password="@20June2005")
ac=a.cursor()

ac.execute("drop database minpro")
print ("Database DROPED")

a.commit()
a.close

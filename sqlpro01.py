import mysql.connector

a=mysql.connector.connect(host="localhost",user="root",password="@20June2005")
ac=a.cursor()

ac.execute("create database MinPro")
print ("Database CREATED")

ac.execute("use MinPro")
print("database in use")

qu="create table parking_span(customer_name char(50),customer_phone1 BigInt,customer_phone2 BigInt,Vehicle_no varchar(10),primary key(vehicle_no))"
ac.execute(qu)
print("table0 created")

qu1="create table parking_span1 (Vehicle_no varchar(10),slot varchar(3),datetime_entry varchar(30),primary key(vehicle_no))"
ac.execute(qu1)
print("table1 created")

qu2="create table parking_span2 (Vehicle_no varchar(10),datetime_exit varchar(30),primary key(vehicle_no))"
ac.execute(qu2)
print("table2 created")

a.commit()
a.close
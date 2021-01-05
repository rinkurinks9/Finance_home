import datetime
import time
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", auth_plugin='mysql_native_password'
                               , database="testdatabase")
my_cursor = mydb.cursor()


'''my_cursor.execute("""CREATE TABLE IF NOT EXISTS PRINCIPLE_AMOUNT(
                    ID int PRIMARY KEY AUTO_INCREMENT,
                    NAME VARCHAR(150),
                    P_AMOUNT float NOT NULL,
                    CREATED VARCHAR(25))""")
mydb.commit()
my_cursor.execute("DESCRIBE PRINCIPLE_AMOUNT")
for x in my_cursor:
    print(x)'''

def Entries():
        name = input("Enter the name of the person to be added : ")
        name_1 = name.replace(" ","_")
        test = name_1.isdigit()
        print(test)
        if test == False:
            print("Name Accepted")
            amount = float(input("Enter the principle amount of the person: "))
            my_cursor.execute("INSERT INTO PRINCIPLE_AMOUNT (NAME,P_AMOUNT,CREATED) VALUES (%s,%s,%s)", (name_1, amount,datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")))
            mydb.commit()
            print("Added to Principle_Amount table")
            my_cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
              ID int PRIMARY KEY AUTO_INCREMENT,
              PRINCIPLE_AMOUNT float NOT NULL,
              WITHDRAW float,
              DEPOSIT float,
              REMARKS VARCHAR(500),
              CREATED VARCHAR(25))""".format(name_1))
            mydb.commit()
            print("Created log with respect to name")
            my_cursor.execute("SHOW TABLES")
            for i in my_cursor:
                print(i)
        else:
            print("Invalid input")

def update():
    id = int(input("Enter the id you want to change : "))
    my_cursor.execute("SELECT * FROM {} WHERE ID = {}".format(name,id))
    print(my_cursor.fetchall())
    pa = float(input("Enter the principle amount : "))
    wd = float(input("Enter the withdraw amount : "))
    dp = float(input("Enter the deposit amount : "))
    rk = input("Enter the remarks : ")
    my_cursor.execute("UPDATE {} SET PRINCIPLE_AMOUNT={}, WITHDRAW={}, DEPOSIT={}, REMARKS='{}',CREATED='{}' WHERE ID = {}".format(name,pa,wd,dp,rk,datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"),id))
    mydb.commit()
    print("CHANGES MADE")
    my_cursor.execute("SELECT * FROM {} WHERE ID = {}".format(name,id))
    print(my_cursor.fetchall())
def update_principle():
        my_cursor.execute("SELECT * FROM PRINCIPLE_AMOUNT WHERE NAME='{}'".format(name))
        for i in my_cursor:
            print(i)
        #id = int(input("Enter the id : "))
        p_amount = float(input("Enter principle amount :"))
        print("amount is : ",p_amount)
        my_cursor.execute("UPDATE PRINCIPLE_AMOUNT SET P_AMOUNT = {},CREATED='{}' WHERE NAME='{}'".format(p_amount,datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"),name))        
        mydb.commit()
        print("completed")
        my_cursor.execute("SELECT * FROM PRINCIPLE_AMOUNT WHERE NAME='{}'".format(name))
        for i in my_cursor:
            print(i)
def display():
        my_cursor.execute("SELECT * FROM PRINCIPLE_AMOUNT WHERE NAME = '{}'".format(name))
        for x in my_cursor:
            print(x)
        my_cursor.execute("SELECT * FROM {}".format(name))
        for x in my_cursor:
            print(x)

def withdraw():
        amount = float(input("Enter the amount you want to withdraw: "))
        comment = input("Enter the reason of withdraw: ")
        my_cursor.execute("SELECT P_AMOUNT FROM PRINCIPLE_AMOUNT WHERE NAME = '{}'".format(name))
        for x in my_cursor:
            y = (x[0])
            if amount > y:
                print("Enter the amount less than principle amount {}".format(y))
            else:
                print("Request is2 executeed")
                deposit = 0
                y = y - amount
                my_cursor.execute("UPDATE PRINCIPLE_AMOUNT SET P_AMOUNT={} WHERE NAME = '{}'".format(y,name))
                mydb.commit()
                my_cursor.execute(
                    "INSERT INTO {} (PRINCIPLE_AMOUNT,WITHDRAW,DEPOSIT,REMARKS,CREATED) VALUES(%s,%s,%s,%s,%s)".format(
                        name), (y, amount, deposit, comment, datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")))
                mydb.commit()
                print(y)

def deposit():
        amount = float(input("Enter the amount you want to deposit: "))
        comment = input("Enter the reason for deposit: ")
        my_cursor.execute("SELECT P_AMOUNT FROM PRINCIPLE_AMOUNT WHERE NAME = '{}'".format(name))
        for x in my_cursor:
            y = (x[0])
            print("Request will be executeed")
            withdraw = 0
            y = y + amount
            my_cursor.execute("UPDATE PRINCIPLE_AMOUNT SET P_AMOUNT={} WHERE NAME = '{}'".format(y,name))
            mydb.commit()
            my_cursor.execute(
                "INSERT INTO {} (PRINCIPLE_AMOUNT,WITHDRAW,DEPOSIT,REMARKS,CREATED) VALUES(%s,%s,%s,%s,%s)".format(
                    name), (y, withdraw, amount, comment,datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")))
            mydb.commit()
            print(y)
def delete():
    
    x = input("Are you sure you want to delete all the records of {} type yes or no".format(name))
    if x == "yes":
        my_cursor.execute("DROP TABLE {}".format(name))
        print("Delete Successful")
    else:
        print("Deleting process stopped.")
    my_cursor.execute("SHOW TABLES")
    for i in my_cursor:
        print(i)

def delete_records():
    my_cursor.execute("SELECT * FROM PRINCIPLE_AMOUNT")
    for x in my_cursor:
        print(x)
    id_num = int(input("Enter the ID number :"))
    my_cursor.execute("DELETE FROM PRINCIPLE_AMOUNT WHERE ID={}".format(id_num))
    mydb.commit()
    print("Deleted Succesufully")
    my_cursor.execute("SELECT * FROM PRINCIPLE_AMOUNT")
    for x in my_cursor:
        print(x) 
#delete_records()

while True:
    try:
        a = int(input('''What do you want to perform 
                      1.Entry 
                      2.Transaction
                      ---->'''))        
    except:
        print("Invalid input")  
    if a==1:
            Entries()
    elif a==2:
             my_cursor.execute("SHOW TABLES")
             for i in my_cursor:
                 print(i)
             x = input("enter the name : ")
             
             name = x.lower()
             if name == "principle_amount":
                display()
                continue
             y = int(input('''WHAT DO YOU WANT TO DO:
              1.WITHDRAWL
              2.DEPOSIT
              3.DISPLAY
              4.DELETE
              5.UPDATE
              6.UPDATE PRINCIPLE
              ---->'''))
             print(name)
             if y==1:
                withdraw()
             if y==2:
                deposit()
             if y ==3:
                display()
             if y==4:
                delete()
             if y==5:
                update()
             if y==6:
                update_principle()
             
                 
   

   


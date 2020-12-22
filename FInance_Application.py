import datetime
#import time
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", auth_plugin='mysql_native_password'
                               , database="testdatabase")
my_cursor = mydb.cursor()


# my_cursor.execute("""CREATE TABLE IF NOT EXISTS PRINCIPLE_AMOUNT(
#                    ID int PRIMARY KEY AUTO_INCREMENT,
#                    NAME VARCHAR(150),
#                    P_AMOUNT float NOT NULL)""")
# mydb.commit()
# my_cursor.execute("DESCRIBE PRINCIPLE_AMOUNT")
# for x in my_cursor:
#    print(x)

def Entries(self):
        self.name = input("Enter the name of the person to be added : ")
        amount = float(input("Enter the principle amount of the person: "))
        my_cursor.execute("INSERT INTO PRINCIPLE_AMOUNT (NAME,P_AMOUNT) VALUES (%s,%s)", (self.name, amount))
        mydb.commit()
        print("Added to Principle_Amount table")
        my_cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
              ID int PRIMARY KEY AUTO_INCREMENT,
              PRINCIPLE_AMOUNT float NOT NULL,
              WITHDRAW float,
              DEPOSIT float,
              REMARKS VARCHAR(500),
              CREATED datetime)""".format(self.name))
        mydb.commit()
        print("Created log with respect to name")
        my_cursor.execute("DESCRIBE {}".format(self.name))
        for x in my_cursor:
            print(x)

    # def update(self):
    #    self.name = input("Enter the name of the person to be updated: ")
    #    my_cursor.execute("ALTER TABLE {} CHANGE first_name PRINCIPLE_AMOUNT FLOAT".format(self.name))
    #    #mydb.commit()
    #    print("CHANGES MADE")
    # def insert(self):
    #    self.name = input("Enter the name you want to insert:")
    #    p_amount = float(input("Enter principle amount :"))
    #    my_cursor.execute("INSERT INTO {} (PRINCIPLE_AMOUNT,CREATED) VALUES (%s,%s)".format(self.name),(p_amount,datetime.datetime.now()))
    #    mydb.commit()
    #    print("completed")
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
                print("Request will be executeed")
                deposit = 0
                y = y - amount
                my_cursor.execute("UPDATE PRINCIPLE_AMOUNT SET P_AMOUNT={} WHERE NAME = '{}'".format(y,name))
                mydb.commit()
                my_cursor.execute(
                    "INSERT INTO {} (PRINCIPLE_AMOUNT,WITHDRAW,DEPOSIT,REMARKS,CREATED) VALUES(%s,%s,%s,%s,%s)".format(
                        name), (y, amount, deposit, comment, datetime.datetime.now()))
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
                    name), (y, withdraw, amount, comment, datetime.datetime.now()))
            mydb.commit()
            print(y)

x = input("enter the name:")
name = x.lower()
while True:
    y = int(input("WHAT DO YOU WANT TO DO:"
              "1.WITHDRAWL"
              "2.DEPOSIT"
              "3.DISPLAY"))

    if y==1:
        withdraw()
    if y==2:
        deposit()
    if y ==3:
        display()


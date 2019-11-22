import pymysql
import hashlib
import os
import time
import getpass
import platform 

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

conn = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "1234",
    database = "Project"
)

c = conn.cursor()

table = """create table if not exists user(
    userid int primary key auto_increment,
    username varchar(50),
    firstname varchar(50),
    surename varchar(50),
    password varchar(50));
"""

c.execute(table)

def encoder(password):
    password = hashlib.md5(password.encode())
    password = password.hexdigest()
    return password


def create_user():
    c = conn.cursor()
    clear()
    found = 0
    password = ''
    pass_again = ' '
    print("Press 'ctrl + c' to exit")
    try:
        while found == 0:
            username = input("Please enter a username: ")
            find_user = (f"select * from user where username like '{username}';")
            c.execute(find_user)
            try:
                a = tuple(tuple(c.fetchall())[0])[1]
            except IndexError:
                a = ""
            if a == username:
                clear()
                print("Username Taken, please try again")
                input()
                clear()
            else:
                found = 1
        firstname = input("Enter your firstname: ")
        surename = input("Enter your surename: ")
        while password != pass_again:
            password = getpass.getpass("Enter your password: ", stream=None)
            pass_again = getpass.getpass("Please re-enter your password: ", stream=None)
            if password != pass_again:
                print("Passwords did not match. Please try again.")
        pass_again = ' '
        password = encoder(password)
        command = f"insert into user values(NULL, '{username}', '{firstname}', '{surename}', '{password}');"
        c.execute(command)
        print("User has been created")
        time.sleep(1)
        main()
        conn.commit()
        conn.close()

    except KeyboardInterrupt:
        print("Exiting...")
        time.sleep(1)
        clear()
        main()

def login():
    c = conn.cursor()
    try:
        clear()
        username = input("Please enter your username: ")
        command = f"SELECT * FROM user WHERE username = '{username}';"
        c.execute(command)
        check = c.fetchone()
        password = getpass.getpass("Please enter your password: ", stream= None)
        password = encoder(password)
        command = f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}';"
        c.execute(command)
        check = c.fetchone()
        if check == None:
            print("Invalid Username or Password. Try again")
            input()
            login()
        else:
            print("You are Logged In!!!")
            input()
            #Type your login function here
            clear()
    except KeyboardInterrupt:
        clear()
        main()

def main():
    clear()
    try:
        print("""
    Enter your choice:
        1. Create User
        2. Login
        3. Exit""")
        opt = input("> ")
        if opt == '1':
            create_user()
            clear()
        elif opt == '2':
            login()
        else:
            exit()
    except KeyboardInterrupt:
        exit()

main()
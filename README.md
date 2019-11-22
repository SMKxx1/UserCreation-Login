# UserCreation-Login
This is a component that you can add to your project to enable user creation and login functionality

## Modules Used:
```
import pymysql
import hashlib
import sys
import os
import time
import getpass
import platform 
```
### **import pymysql**
* [pymysql](https://pypi.org/project/PyMySQL/) - For MYSQL connection
```
conn = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "1234",
    database = "Project"
)

c = conn.cursor()
```
Please ignore `port = 3306` argument.

`passwd = "1234"` is the same as `password = "1234"`.

### __import hashlib__
* [hashlib](https://pypi.org/project/hashlib/) - For hashing/encoding the password
```
def encoder(password):
    password = hashlib.md5(password.encode())
    password = password.hexdigest()
    return password
```
Creating a Function called encoder so that we can cut time in encoding passwords.

`password = hashlib.md5(password.encode())` here `hashlib.md5` is used to convert the password
to a md5 hash but it only works with utf-8 strings and since python uses unicode to store its strings
we will have to convert it to utf-8 using the command `.encode()`.

### __import os__
* [os](https://docs.python.org/3.7/library/os.html) - For clearing the screen
```
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
```
There are a million things you can do with os module but here we will be using it to clear the screen.
The clear screen command is different on windows, mac and linux so we use the platform module to find the 
operating system. Then a command corresponding to the operating system being used.
* Windows - `os.system('cls')`
* Mac/Linux - `os.system('clear')`


### __import time__
* [time](https://docs.python.org/3.7/library/time.html) - For sleep function
```
time.sleep(1)
```
`time.sleep()` takes a number as an argument. This number is the amount of seconds that the program will freez for.


### __import getpass__
* [getpass](https://docs.python.org/3.7/library/getpass.html) - For getting the password without ECHO
```
password = getpass.getpass("Enter your password: ", stream=None)
```
This is a module 
### __import platform__
* [platform](https://docs.python.org/3.7/library/platform.html) - For identifying the operating system
```
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
```

# MYSQL
## User Table
`desc user;`

| Field     | Type        | Null | Key | Default | Extra          |
|-----------|-------------|------|-----|---------|----------------|
| userid    | int(11)     | NO   | PRI | NULL    | auto_increment |
| username  | varchar(50) | YES  |     | NULL    |                |
| firstname | varchar(50) | YES  |     | NULL    |                |
| surename  | varchar(50) | YES  |     | NULL    |                |
| password  | varchar(50) | YES  |     | NULL    |                |


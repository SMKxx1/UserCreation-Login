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
### _pymysql_
[pymysql](https://pypi.org/project/PyMySQL/) - For MYSQL connection
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
### _hashlib_
* [hashlib](https://pypi.org/project/hashlib/) - For hashing/encoding the password
```
def encoder(password):
    password = hashlib.md5(password.encode())
    password = password.hexdigest()
    return password
```
### _os_
* [os](https://docs.python.org/3.7/library/os.html) - For clearing the screen
```
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
```
### _time_
* [time](https://docs.python.org/3.7/library/time.html) - For sleep function
```
time.sleep(1)
```
### _getpass_
* [getpass](https://docs.python.org/3.7/library/getpass.html) - For getting the password without ECHO
```
password = getpass.getpass("Enter your password: ", stream=None)
```


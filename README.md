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
### _sys_

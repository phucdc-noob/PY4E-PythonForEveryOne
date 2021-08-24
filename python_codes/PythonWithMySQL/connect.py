# pip install mysql-connector-python
'''
- To create new user, after install mysql (or mariaDB), open Terminal, then complete setup by command: mysql_secure_installation (1)
- After finishing the installation, enter command: mysql -u root -p   then enter the root password you set in (1).
- Enter command: create user '<username>'@'localhost' identified by '<password>';
- To grant all privileges to new user:
    grant all privileges on *.* to '<username>'@'localhost';
- I don't recommend you to grant all privileges to user, except that is admin's user.
- Then login to new user by: mysql -u <username> -p<password>
- Create new database: create database <db_name>;
- You can check databases that user can access by: show databases;
'''
import mysql.connector as mysql

'''
create a cursor to connect to localhost:3306//python with user python
'''
try:
    conn = mysql.connect(
        host = "localhost",
        user = "python",
        password = "python",
        database = "python"
    )
    print('Connected successfully')
except mysql.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
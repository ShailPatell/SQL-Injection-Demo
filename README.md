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

###2. Multi-Statement Support
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

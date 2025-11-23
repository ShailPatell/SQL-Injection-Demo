DROP DATABASE IF EXISTS injection_demo;
CREATE DATABASE injection_demo;
USE injection_demo;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO users (username, password)
VALUES ('admin', 'admin123'), ('test', 'test123'), ('shail', 'shail123');

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    price DECIMAL(10,2)
);

INSERT INTO products (name, price)
VALUES ('Laptop', 899.99), ('Mouse', 19.99);

CREATE TABLE logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username_attempt VARCHAR(50),
    success BOOLEAN,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP DATABASE IF EXISTS icecream_db;
CREATE DATABASE icecream_db;
USE icecream_db;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    created_at DATETIME
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    flavor VARCHAR(50),
    scoops INT,
    price DECIMAL(5,2),
    order_time DATETIME,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers VALUES
(1, 'Alice Key', 'alice@example.com', NOW()),
(2, 'Bob Smith', 'bob@example.com', NOW()),
(3, 'Carla Nguyen', 'carla@example.com', NOW()),
(4, 'David Lee', 'david@example.com', NOW()),
(5, 'Emma Brown', 'emma@example.com', NOW()),
(6, 'Frank Moore', 'frank@example.com', NOW()),
(7, 'Grace Kim', 'grace@example.com', NOW()),
(8, 'Henry Patel', 'henry@example.com', NOW()),
(9, 'Isabel Garcia', 'isabel@example.com', NOW()),
(10, 'Jack Wilson', 'jack@example.com', NOW());

INSERT INTO orders VALUES
(101, 1, 'Vanilla', 2, 5.50, NOW()),
(102, 2, 'Chocolate', 3, 7.25, NOW()),
(103, 3, 'Strawberry', 1, 3.00, NOW()),
(104, 4, 'Mint Chip', 2, 5.75, NOW()),
(105, 5, 'Cookie Dough', 3, 7.50, NOW()),
(106, 6, 'Vanilla', 1, 2.75, NOW()),
(107, 7, 'Rocky Road', 2, 6.00, NOW()),
(108, 8, 'Chocolate', 1, 3.25, NOW()),
(109, 9, 'Strawberry', 3, 7.00, NOW()),
(110, 10, 'Mango Sorbet', 2, 5.50, NOW());

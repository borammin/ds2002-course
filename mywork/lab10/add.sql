USE tsc9rv_db;

DELETE FROM customers WHERE customer_id IN (15,16,17,18,19,20);

INSERT INTO customers (customer_name, email, created_at) VALUES
('Liam Turner', 'liam2@example.com', NOW()),
('Mia Davis', 'mia2@example.com', NOW()),
('Noah White', 'noah2@example.com', NOW());

INSERT INTO orders (order_id, customer_id, flavor, scoops, price, order_time) VALUES
(113, 13, 'Strawberry', 1, 3.50, NOW()),
(114, 11, 'Mint Chip', 2, 5.75, NOW());

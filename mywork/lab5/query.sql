USE icecream_db;

SELECT
    c.customer_name,
    o.flavor,
    o.scoops,
    o.price
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.scoops >= 2;
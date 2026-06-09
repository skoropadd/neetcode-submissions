-- Write your query below
SELECT 
a.name
FROM customers as a
LEFT JOIN orders as b on a.id = b.customer_id
WHERE b.id is NULL
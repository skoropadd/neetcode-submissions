-- Write your query below
WITH cte AS (
    SELECT 
    a.customer_id, 
    c.name, 
    a.order_id, 
    EXTRACT(MONTH from order_date) as order_month,
    (a.quantity * b.price) as spent
    FROM orders as a 
    LEFT JOIN product as b ON a.product_id = b.product_id
    LEFT JOIN customers as c ON c.customer_id = a.customer_id
    WHERE a.order_date BETWEEN '2020-06-01' AND '2020-07-31'
)

SELECT 
customer_id, 
name
FROM CTE 
GROUP BY customer_id, name 
HAVING SUM(CASE WHEN order_month = 6 then spent else 0 END) >= 100 
AND SUM(CASE WHEN order_month = 7 then spent else 0 END) >= 100
-- Write your query below
WITH cte as (
    SELECT 
        customer_id, 
        CASE WHEN product_name = 'A' then 1 else 0 end as have_a, 
        CASE WHEN product_name = 'B' then 1 else 0 end as have_b, 
        CASE WHEN product_name = 'C' then 1 else 0 end as have_c
    FROM orders
)
SELECT 
    a.customer_id, 
    b.customer_name
FROM cte as a 
LEFT JOIN customers as b
    ON a.customer_id = b.customer_id
GROUP BY a.customer_id, b.customer_name
HAVING sum(have_a) > 0 AND sum(have_b) > 0 AND sum(have_c) = 0 
ORDER BY b.customer_name

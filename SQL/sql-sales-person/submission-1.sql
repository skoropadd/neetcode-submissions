-- Write your query below
WITH cte AS (
    SELECT 
    a.sales_id
    FROM orders as a
    INNER JOIN company as b ON a.com_id = b.com_id and b.name = 'CRIMSON'
) 

SELECT 
a.name 
FROM sales_person as a 
WHERE a.sales_id NOT IN (SELECT * FROM cte)
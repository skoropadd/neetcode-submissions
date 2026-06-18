-- Write your query below
SELECT 
a.sale_date, 
a.sold_num - b.sold_num as diff
FROM sales AS a 
LEFT JOIN sales AS b ON a.sale_date = b.sale_date and b.fruit = 'oranges'
WHERE a.fruit = 'apples'
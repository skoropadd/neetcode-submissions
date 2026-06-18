-- Write your query below
SELECT 
    a.seller_name
FROM seller as a 
LEFT JOIN orders as b ON a.seller_id = b.seller_id and b.sale_date between '2020-01-01' and '2020-12-31'
GROUP BY a.seller_id
HAVING COALESCE(count(order_id), 0) = 0
ORDER BY a.seller_name

SELECT o.customer_id, c.customer_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY o.customer_id, c.customer_name
HAVING SUM(CASE WHEN product_name = 'A' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN product_name = 'B' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN product_name = 'C' THEN 1 ELSE 0 END) = 0
ORDER BY c.customer_name;
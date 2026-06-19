-- Write your query below
SELECT 
b.name, 
COALESCE(SUM(a.distance), 0) as travelled_distance
FROM users as b 
LEFT JOIN rides as a ON b.id = a.user_id
GROUP BY b.name
ORDER BY COALESCE(SUM(a.distance), 0) DESC
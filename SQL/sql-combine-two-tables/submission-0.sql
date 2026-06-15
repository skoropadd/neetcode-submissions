-- Write your query below
SELECT 
first_name, 
last_name, 
city, 
state
FROM person as a 
LEFT JOIN address as b ON a.person_id = b.person_id

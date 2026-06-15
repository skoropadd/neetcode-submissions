-- Write your query below
SELECT 
left_operand, 	
operator, 	
right_operand, 
case 
    when operator = '>' AND b.value > c.value then 'true'
    when operator = '=' AND b.value = c.value then 'true'
    when operator = '<' AND b.value < c.value then 'true'
    ELSE 'false'
END AS value
FROM expressions as a 
LEFT JOIN variables as b on a.left_operand = b.name
LEFT JOIN variables as c on a.right_operand = c.name

-- Write your query below

--- lets find all the leafs 
WITH leafs AS (
    SELECT id 
    FROM tree
    WHERE id NOT IN (SELECT p_id FROM tree WHERE p_id IS NOT NULL)
)

SELECT 
    id, 
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT id FROM leafs) THEN 'Leaf'
        ELSE 'Inner' 
    END as type
FROM tree

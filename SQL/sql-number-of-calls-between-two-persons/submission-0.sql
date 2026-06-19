-- Write your query below
WITH cte as (
    SELECT 
        a.from_id AS person1, 
        a.to_id AS person2, 
        COUNT(a.duration) AS call_count,
        SUM(a.duration) AS total_duration
    FROM calls AS a
    WHERE a.from_id < a.to_id
    GROUP BY a.from_id, a.to_id
    UNION ALL
    SELECT 
        a.to_id AS person1, 
        a.from_id AS person2, 
        COUNT(a.duration) AS call_count,
        SUM(a.duration) AS total_duration
    FROM calls AS a
    WHERE a.from_id > a.to_id
    GROUP BY a.from_id, a.to_id
)

SELECT 
person1, 
person2, 
SUM(call_count) AS call_count, 
SUM(total_duration) AS total_duration
FROM cte
GROUP BY person1, person2
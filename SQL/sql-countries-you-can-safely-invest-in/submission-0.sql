-- Write your query below
WITH call_country AS (
    SELECT c.duration, co.name as country
    FROM calls as c
    JOIN person as p
        ON p.id IN (c.caller_id, c.callee_id)
    JOIN country as co
        ON co.country_code = SUBSTRING(p.phone_number, 1, 3)
)
SELECT
    country
FROM call_country
GROUP BY country
HAVING avg(duration) > (SELECT avg(duration) FROM calls)
-- Write your query below
WITH cte AS (
    SELECT 
    match_id, 
    host_team, 
    guest_team, 
    host_goals, 
    guest_goals, 
    CASE 
        WHEN host_goals > guest_goals then 3
        WHEN host_goals = guest_goals then 1
        WHEN host_goals < guest_goals then 0
    END as host_points, 
    CASE 
        WHEN host_goals < guest_goals then 3
        WHEN host_goals = guest_goals then 1
        WHEN host_goals > guest_goals then 0
    END as guest_points
    FROM matches
),

stat AS (
    SELECT 
        a.host_team AS team_id,
        a.host_points AS num_points
    FROM cte as a
    UNION ALL
    SELECT 
        b.guest_team AS team_id,
        b.guest_points AS num_points
    FROM cte as b
),

agg AS (
    SELECT 
    team_id, 
    sum(num_points) as num_points
    FROM stat
    GROUP BY team_id
)

SELECT 
t.team_id, 
t.team_name, 
COALESCE(a.num_points, 0) as num_points
FROM teams as t
LEFT JOIN agg as a on a.team_id = t.team_id
ORDER BY num_points DESC
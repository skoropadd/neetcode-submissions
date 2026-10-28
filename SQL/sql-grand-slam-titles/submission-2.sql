-- Write your query below
WITH champions AS (
    SELECT 
        year,
        wimbledon as winner_id 
    FROM championships
        UNION ALL 
    SELECT 
        year,
        fr_open as winner_id 
    FROM championships
        UNION ALL 
    SELECT 
        year,
        us_open as winner_id 
    FROM championships
        UNION ALL 
    SELECT 
        year,
        au_open as winner_id 
    FROM championships
)

SELECT 
    c.winner_id as player_id,
    p.player_name as player_name, 
    count(c.*) as grand_slams_count
FROM champions as c 
JOIN players as p 
    ON c.winner_id = p.player_id
GROUP BY winner_id, p.player_name
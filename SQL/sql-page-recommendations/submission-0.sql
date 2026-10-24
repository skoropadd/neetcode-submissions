-- Write your query below

--- user_1 friends 
WITH friends AS (
    SELECT user1_id as friend
    FROM friendship
    WHERE user2_id = 1 
    UNION ALL 
    SELECT user2_id as friend
    FROM friendship
    WHERE user1_id = 1
)

---- what friends like
SELECT DISTINCT(l.page_id) as recommended_page
FROM likes as l 
JOIN friends as f
    ON f.friend = l.user_id
WHERE l.page_id NOT IN (SELECT page_id FROM likes WHERE user_id = 1)

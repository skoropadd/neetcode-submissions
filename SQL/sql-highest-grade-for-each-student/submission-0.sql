-- Write your query below
WITH cte as (
    SELECT 
        student_id, 
        exam_id, 
        score, 
        ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY score DESC, exam_id ASC) as rn
    FROM exam_results
    ORDER BY student_id
)
SELECT 
student_id, 
exam_id, 
score
FROM cte 
WHERE rn = 1
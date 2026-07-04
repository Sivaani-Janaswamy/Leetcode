# Write your MySQL query statement below
SELECT contest_id,ROUND((contest_count/(SELECT COUNT(*) FROM Users))*100,2) AS percentage 
FROM 
( 
    SELECT contest_id, COUNT(user_id) AS contest_count
    FROM Register
    GROUP BY contest_id
) AS temp
ORDER BY percentage DESC, contest_id ASC;
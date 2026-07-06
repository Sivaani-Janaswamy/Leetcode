SELECT DISTINCT c.num AS  ConsecutiveNums
FROM Logs c
LEFT JOIN Logs p
ON c.id-1=p.id
LEFT JOIN Logs n
ON c.id+1=n.id
WHERE p.num = c.num AND c.num = n.num;


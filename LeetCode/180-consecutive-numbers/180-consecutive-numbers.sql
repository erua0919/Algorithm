# Write your MySQL query statement below
SELECT DISTINCT l.num  AS ConsecutiveNums 
	FROM logs AS l
    		INNER JOIN logs AS l_next ON l.id + 1 = l_next.id 
    		INNER JOIN logs As l_next2 ON l_next.id +1 = l_next2.id 
WHERE l.num = l_next.num AND l_next.num = l_next2.num 
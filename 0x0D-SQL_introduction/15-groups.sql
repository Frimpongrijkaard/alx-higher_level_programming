-- lists the number of records with same score
--in the second table of the hbtn_0c_0
-- in MySQL server
SELECT score, COUNT('count') AS number FROM second_table
GROUP BY score
ORDER BY score DESC;
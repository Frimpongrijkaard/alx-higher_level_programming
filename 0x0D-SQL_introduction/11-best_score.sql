-- Lists all records score greater tha 10
-- in the second table of hbtn_0c_0 in mySQL server
-- should be ordered
-- with score >= 10
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

-- lists all record of the table
-- dont lists row without a name
-- result should display the score and name
-- should listed by descending
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

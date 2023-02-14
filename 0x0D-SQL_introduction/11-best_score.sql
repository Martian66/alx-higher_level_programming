-- A script that lists all records with a score >= 10
-- Results should display both the score and name in descending order

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC, name;

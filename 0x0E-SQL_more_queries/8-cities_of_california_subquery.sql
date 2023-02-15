-- A script that lists all the cities of California of the database
-- Results must be sorted in ascending order
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id;

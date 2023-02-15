-- A script that creates a database and user
-- The user should only have SELECT privileges in the database
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
GRANT SELECT ON *.* TO 'user_0d_1'@'localhost';

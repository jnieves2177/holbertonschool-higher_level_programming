-- Create a new table
CREATE TABLE IF NOT EXISTS second_table
(id INT,
 name VARCHAR(256),
 score INT);
-- Insert first row into the table
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10);
-- Insert second row into the table
INSERT INTO second_table (id, name, score)
VALUES (2, 'Alex', 3);
-- Insert third row into the table
INSERT INTO second_table (id, name, score)
VALUES (3, 'Bob', 14);
-- Insert fourth row into the table
INSERT INTO second_table (id, name, score)
VALUES (4, 'George', 8);
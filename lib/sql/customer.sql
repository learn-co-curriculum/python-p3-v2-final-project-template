DROP TABLE IF EXISTS customer;

CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

INSERT INTO customer (name, age)
VALUES ("Lulu", 20),
("Betsy", 35),
("Rick", 28),
("Jessica", 19);


DELETE FROM customer
WHERE age < 21;

SELECT * FROM customer
WHERE age > 21;
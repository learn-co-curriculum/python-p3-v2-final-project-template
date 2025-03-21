DROP TABLE IF EXISTS drinks;

CREATE TABLE IF NOT EXISTS drinks (
    id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO drinks (name)
VALUES ("Mojito"),
("Long Island"),
("Mai Thai"),
("Titos & Soda");

DELETE FROM drinks
WHERE name = "Long Island";

SELECT * FROM drinks
WHERE name = name
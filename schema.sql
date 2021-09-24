CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product TEXT,
    since DATE,
    until DATE,
    visible BOOLEAN NOT NULL
);

INSERT INTO products (product, since, until, visible)
VALUES ('strawberry cake', '01/01/2015', NULL , True),
('blueberry cake', '01/01/2015', NULL , True),
('cranberry cookies', '01/06/2015', NULL , True),
('rye bread', '01/06/2017', NULL , True),
('chocolate bread', '01/08/2018', NULL , True),
('cranberry yoghurt', '01/06/2018', NULL , True),
('banana yoghurt', '01/06/2018', NULL , True),
('fruit energy bar', '15/06/2020', NULL , True),
('chocolate energy bar', '01/06/2021', NULL , True),
('coffee energy bar', '01/06/2021', NULL , True);

CREATE TABLE ideas (
    id SERIAL PRIMARY KEY,
    idea TEXT,
    datum DATE NOT NULL DEFAULT CURRENT_DATE,
    short_list BOOLEAN NOT NULL,
    visible BOOLEAN NOT NULL
);
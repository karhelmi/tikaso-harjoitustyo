DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

DROP TABLE IF EXISTS products CASCADE;

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product TEXT UNIQUE,
    since DATE,
    until DATE,
    visible BOOLEAN DEFAULT TRUE
);

INSERT INTO products (product, since, until, visible)
VALUES ('strawberry cake', '01/01/2015', NULL , True),
('blueberry cake', '01/01/2015', NULL , True),
('cranberry cookies', '01/06/2015', NULL , True),
('rye bread', '01/06/2017', NULL , True),
('chocolate bread', '01/08/2018', NULL , True),
('cranberry yoghurt', '01/06/2018', NULL , True),
('banana yoghurt', '01/06/2018', NULL , True),
('fruit energy bar', '10/06/2020', NULL , True),
('chocolate energy bar', '01/06/2021', NULL , True),
('coffee energy bar', '01/06/2021', NULL , True);

DROP TABLE IF EXISTS ideas CASCADE;

CREATE TABLE ideas (
    id SERIAL PRIMARY KEY,
    userid INTEGER REFERENCES users,
    product_id INTEGER REFERENCES products,
    idea TEXT,
    datum DATE DEFAULT CURRENT_DATE,
    visible BOOLEAN DEFAULT TRUE
);

DROP TABLE IF EXISTS projects CASCADE;

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    idea_id INTEGER REFERENCES ideas,
    project_team_id INTEGER REFERENCES teams,
    start_datum DATE NOT NULL,
    target_datum DATE NOT NULL,
    completed BOOLEAN NOT NULL,
    visible BOOLEAN DEFAULT TRUE
);

DROP TABLE IF EXISTS teams CASCADE;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    team_name TEXT,
    visible BOOLEAN DEFAULT TRUE
);

DROP TABLE IF EXISTS employees CASCADE;

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

INSERT INTO employees (first_name, last_name)
VALUES ('Donald', 'Duck'),
('Daisy', 'Duck'),
('Huey', 'Duck'),
('Dewey', 'Duck'),
('Louie', 'Duck'),
('Goofy', 'Goofison'),
('Mickey', 'Mouse'),
('Pluto', 'Dog');

DROP TABLE IF EXISTS team_members CASCADE;

CREATE TABLE team_members (
    id SERIAL PRIMARY KEY,
    team_id INTEGER REFERENCES teams,
    employee_id INTEGER REFERENCES employees
);



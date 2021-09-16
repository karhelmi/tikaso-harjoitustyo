CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
    icecream TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    product TEXT,
    since DATE,
    until DATE,
    visible BOOLEAN NOT NULL
);

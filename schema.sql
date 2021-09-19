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

CREATE TABLE testi (
    id SERIAL PRIMARY KEY,
    sana TEXT
);

CREATE DATABASE test_db;

-----------


CREATE TABLE IF NOT EXISTS book(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	date DATE,
	price FLOAT,
	language VARCHAR(31)
);

CREATE TABLE IF NOT EXISTS author(
	id SERIAL PRIMARY KEY,
	name VARCHAR(127) NOT NULL,
	last_name VARCHAR(127) NOT NULL,
	age INTEGER
);

CREATE TABLE IF NOT EXISTS book_author(
	author_id INTEGER,
	book_id INTEGER,
	PRIMARY KEY(author_id, book_id),
	FOREIGN KEY (author_id) REFERENCES author(id),
	FOREIGN KEY (book_id) REFERENCES book(id)
);
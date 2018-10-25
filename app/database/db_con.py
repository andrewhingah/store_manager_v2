
import os

def migrate():
    from .. import db
    conn = db.conn
    cur = db.cursor

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    	id serial PRIMARY KEY,
    	name varchar,
    	email varchar UNIQUE,
        username varchar,
    	password varchar
    	);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS products(
        id serial PRIMARY KEY,
        name varchar,
        quantity numeric NOT NULL,
        price numeric NOT NULL,
        date_posted TIMESTAMP,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id)
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sales(
        id serial PRIMARY KEY,
        product_id INT,
        quantity numeric NOT NULL,
        price numeric NOT NULL,
        date_posted TIMESTAMP,
        category varchar,
        FOREIGN KEY (product_id) REFERENCES products(id)
        );""")
    
    print("Database connected")
    
    conn.commit()


    
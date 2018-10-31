
import os

def reset_migrations():
    from app import db
    conn = db.conn
    cur = db.cursor

    cur.execute("""DELETE FROM sales;""")

    cur.execute("""DELETE FROM products;""")

    cur.execute("""DELETE FROM users;""")

    conn.commit()


def migrate():
    from app import db
    conn = db.conn
    cur = db.cursor

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    	id serial PRIMARY KEY,
        name varchar,
        email varchar UNIQUE,
    	password varchar,
        role varchar
    	);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS products(
        id serial PRIMARY KEY,
        name varchar,
        category varchar,
        quantity INT NOT NULL,
        price INT NOT NULL,
        date_created TIMESTAMP,
        user_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sales(
        id serial PRIMARY KEY,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        remaining_q INT NOT NULL,
        price INT NOT NULL,
        name varchar,
        date_created TIMESTAMP,  
        FOREIGN KEY (product_id) REFERENCES products(id)
        );""")
    
    print("Database connected")
    
    conn.commit()


    
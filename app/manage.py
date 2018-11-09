"""Create tables, delete from tables"""

def reset_migrations():
    '''clear tables after tests'''
    from app import db
    conn = db.conn
    cur = db.cursor

    cur.execute("""DELETE FROM sales;""")

    cur.execute("""DELETE FROM products;""")

    cur.execute("""DELETE FROM users;""")

    conn.commit()


def migrate():
    '''create tables and columns'''
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

    #create default admin
    # cur.execute("""INSERT INTO users(name, email, password, role) VALUES(
    #     'Andrew Hinga', 'andrewhinga@store.com','A123@admin','admin') ON CONFLICT DO NOTHING;""")
    # conn.commit()
    cur.execute("""INSERT INTO users (name, email, password,role) SELECT 'superadmin','super@admin.com','A123@admin','admin' WHERE 'super@admin.com' NOT IN
        (
        SELECT email FROM users
        );""")
    conn.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS products(
        id serial PRIMARY KEY,
        name varchar,
        category varchar,
        quantity INT NOT NULL,
        price INT NOT NULL,
        date_created TIMESTAMP
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sales(
        id serial PRIMARY KEY,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        remaining_q INT NOT NULL,
        price INT NOT NULL,
        name varchar,
        date_created TIMESTAMP
        );""")
    
    print("Database connected")
    
    conn.commit()


    
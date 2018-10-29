'''helper functions for models'''
import datetime
import psycopg2
import os
from app import db

conn = db.conn
cur = db.cursor


def insert_user(users):
    cur.execute("""INSERT INTO users(name, email, password) VALUES('%s', '%s', '%s');"""%(
        users.name,
        users.email,
        users.password))
    conn.commit()

def get_user(email):
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    if user is None:
        return None
    conn.commit()
    return user

def create_product(products):
    cur.execute("""INSERT INTO products(category, name, quantity, price, date_created, user_id) VALUES(
        '%s','%s','%s','%s', now(), '%s') """%(
        products.category,
        products.name,
        products.quantity,
        products.price,
        products.user_id))
    conn.commit()

def get_products():
    cur.execute("SELECT * FROM PRODUCTS")
    products = cur.fetchall()
    rows = []
    for row in products:
        rows.append(dict(row))
    if rows is None:
        return None  
    conn.commit()
    return rows

def get_product(id):
    cur.execute("SELECT * FROM PRODUCTS WHERE id = %s", (id,))
    product = cur.fetchone()
    if product is None:
        return None
    conn.commit()
    return product

def edit_product(id, product):
    cur.execute("UPDATE products SET category = %s, name = %s, quantity = %s, price = %s, date_posted = %s WHERE id = %s", (
        product['category'],
        product['name'],
        product['quantity'],
        product['price'],
        product['date_posted'],
        id))
    conn.commit()

def delete_product(id):
    cur.execute("DELETE FROM products WHERE id = %s", (id,))
    conn.commit()
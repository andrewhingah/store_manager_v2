'''helper functions for models'''
import datetime
import psycopg2
import os
from app import db

conn = db.conn
cur = db.cursor

def insert_user(users):
    '''save new user to db'''
    cur.execute("""INSERT INTO users(name, email, password, role) VALUES('%s', '%s','%s','%s');"""%(
        users.name,
        users.email,
        users.password,
        users.role))
    conn.commit()


def get_user(email):
    '''retrieve a single user from db'''
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    if user is None:
        return None
    conn.commit()
    return user

def create_product(products):
    '''save new product to db'''
    cur.execute("""INSERT INTO products(category, name, quantity, price, date_created) VALUES(
        '%s','%s','%s','%s', now()) """%(
        products.category,
        products.name,
        products.quantity,
        products.price))
    conn.commit()

def get_products():
    '''fetch products from db'''
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    rows = []
    for row in products:
        rows.append(dict(row))
    if rows is None:
        return None  
    conn.commit()
    return rows

def get_product(id):
    '''fetch single product from db'''
    cur.execute("SELECT * FROM products WHERE id = %s", (id,))
    product = cur.fetchone()
    if product is None:
        return None
    conn.commit()
    return product

def edit_product(id, product):
    '''modify a product details'''
    cur.execute("UPDATE products SET category = %s, name = %s, quantity = %s, price = %s, date_created = %s WHERE id = %s", (
        product['category'],
        product['name'],
        product['quantity'],
        product['price'],
        product['date_created'],
        id))
    conn.commit()

def decrease_quantity(id, product):
    '''decrease quantity of product after sale'''
    cur.execute("UPDATE products SET quantity = %s WHERE id = %s", (
        product['quantity'],
        id))
    conn.commit()

def delete_product(id):
    '''delete product from db'''
    cur.execute("DELETE FROM products WHERE id = %s", (id,))
    conn.commit()

def create_sale(sales):
    '''save a sale record to db'''
    cur.execute("""INSERT INTO sales(product_id, quantity, remaining_q, price, name, date_created) VALUES(
        '%s','%s','%s','%s', '%s', now()) """%(
        sales.product_id,
        sales.quantity,
        sales.remaining_q,
        sales.price,
        sales.name))
    conn.commit()

def get_sales():
    '''fetch sales from db'''
    cur.execute("SELECT * FROM sales")
    sales = cur.fetchall()
    rows = []
    for row in sales:
        rows.append(dict(row))
    if rows is None:
        return None  
    conn.commit()
    return rows

def get_sale(id):
    '''fetch single sale from db'''
    cur.execute("SELECT * FROM sales WHERE id = %s", (id,))
    sale = cur.fetchone()
    if sale is None:
        return None
    conn.commit()
    return sale
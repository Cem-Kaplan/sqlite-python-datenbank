import sqlite3

connection = sqlite3.connect("produkte.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS produkte (number INTEGER PRIMARY KEY, name TEXT, price FLOAT)")
connection.commit()

def add_new_product(name, price):
    cursor.execute("INSERT INTO produkte (name, price) VALUES (?, ?)", (name, price))

def show_products():
    cursor.execute("SELECT * FROM produkte")
    for eintrag in cursor:
        print(eintrag)

add_new_product("PC", 200.00)
add_new_product("Bread", 5.99)
show_products()
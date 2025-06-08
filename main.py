import sqlite3, tkinter

tk = tkinter.Tk()
tk.title("Datenbank mit sqlite")

connection = sqlite3.connect("produkte.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS produkte (number INTEGER PRIMARY KEY, name TEXT, price FLOAT)")
connection.commit()

def add_new_product(name, price):
    cursor.execute("INSERT INTO produkte (name, price) VALUES (?, ?)", (name, price))

def show_products_in_cmd():
    cursor.execute("SELECT * FROM produkte")
    for eintrag in cursor:
        print(eintrag)

def show_products_in_ui():
    cursor.execute("SELECT * FROM produkte")
    for eintrag in cursor:
        table = tkinter.Label(text=eintrag, width=100)
        table.pack()

add_new_product("PC", 200.00)
add_new_product("Bread", 5.99)
show_products_in_cmd()
show_products_in_ui()

tk.mainloop()
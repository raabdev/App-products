from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    db_name = 'database.db'

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_products(self):
        #limpiando la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #obteniendo datos
        query = 'SELECT * FROM product ORDER BY nombre DESC'
        db_rows = self.run_query(query)
        #rellenando datos
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')

        #Crear el Frame container
        frame = LabelFrame(self.wind, text = 'Registre un nuevo producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Name input
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        #Price input
        Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        #Boton agregar
        ttk.Button(frame, text = 'Guardar producto').grid(row = 3, columnspan = 2, sticky = W + E)

        #Tabla
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'Precio', anchor = CENTER)

        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()

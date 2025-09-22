from tkinter import *

from functools import partial

import time

import pymysql.cursors
# import only system from os


def ingresar():

    def empleado():

        def enter():

            caEmple.grid_forget()

            cursor.execute("Insert into empleado(dni,sueldo,rol,nombre,descuento) values ('"+dni.get() + "','" +
                           sueldo.get() + "','" + rol.get() + "','" + nombre.get() + "','" + descuento.get() + "'"");")
            # seinsertan los valosres, copiar y pegar con el resto de las tablas

            connection.commit()

            btEnter.grid_forget()

            root.destroy()

        btTablas.grid_forget()

        Label(caEmple, text='Dni').grid(row=0)
        Label(caEmple, text='Sueldo').grid(row=1)
        Label(caEmple, text='Rol').grid(row=2)
        Label(caEmple, text='Nombre').grid(row=3)
        Label(caEmple, text='Descuento').grid(row=4)

        dni = Entry(caEmple)
        sueldo = Entry(caEmple)
        rol = Entry(caEmple)
        nombre = Entry(caEmple)
        descuento = Entry(caEmple)

        dni.grid(row=0, column=1)
        sueldo.grid(row=1, column=1)
        rol.grid(row=2, column=1)
        nombre.grid(row=3, column=1)
        descuento.grid(row=4, column=1)

        btEnter = Button(root, text="enter", command=enter,
                         bg="Black", fg="white")

        btEnter.grid(row=50, column=70)

    def ingrediente():

        def enter():

            caIngred.grid_forget()

            cursor.execute("Insert into ingrediente(nombre,stock,unidad) values ('" +
                           nombre.get() + "','" + stock.get() + "','" + unidad.get() + "'"");")
        # se insertan los valosres, copiar y pegar con el resto de las tablas

            connection.commit()

            btEnter.grid_forget()

            root.destroy()

        btTablas.grid_forget()

        Label(caIngred, text='Ingrediente').grid(row=0)
        Label(caIngred, text='Stock').grid(row=1)
        Label(caIngred, text='Unidad').grid(row=2)

        nombre = Entry(caIngred)
        stock = Entry(caIngred)
        unidad = Entry(caIngred)

        nombre.grid(row=0, column=1)
        stock.grid(row=1, column=1)
        unidad.grid(row=2, column=1)

        btEnter = Button(root, text="enter", command=enter,
                         bg="Black", fg="white")

        btEnter.grid(row=50, column=70)

    def prodIngr():

        def enter():

            caProdIngred.grid_forget()

            cursor.execute("Insert into ingrediente(idProducto,idIngr,cant) values ('" +
                           idProducto.get() + "','" + idIngr.get() + "','" + cant.get() + "'"");")
        # se insertan los valosres, copiar y pegar con el resto de las tablas

            connection.commit()

            btEnter.grid_forget()

            root.destroy()

        btTablas.grid_forget()

        Label(caProdIngred, text='idProducto').grid(row=0)
        Label(caProdIngred, text='idIngr').grid(row=1)
        Label(caProdIngred, text='cant').grid(row=2)

        nombre = Entry(caProdIngred)
        stock = Entry(caProdIngred)
        cant = Entry(caProdIngred)

        nombre.grid(row=0, column=1)
        stock.grid(row=1, column=1)
        cant.grid(row=2, column=1)

        btEnter = Button(root, text="enter", command=enter,
                         bg="Black", fg="white")

        btEnter.grid(row=50, column=70)

    def venta():

        def enter():

            caVenta.grid_forget()

            cursor.execute("Insert into venta(idVenta,fecha,dni,monto) values ('" + idVenta.get(
            ) + "','" + fecha.get() + "','" + dni.get() + "','"+monto.get()+"'"");")
        # se insertan los valosres, copiar y pegar con el resto de las tablas

            connection.commit()

            btEnter.grid_forget()

            root.destroy()

        btTablas.grid_forget()

        Label(caVenta, text='idVenta').grid(row=0)
        Label(caVenta, text='fecha').grid(row=1)
        Label(caVenta, text='dni').grid(row=2)
        Label(caVenta, text='monto').grid(row=2)

        idVenta = Entry(caVenta)
        fecha = Entry(caVenta)
        dni = Entry(caVenta)
        monto = Entry(caVenta)

        idVenta.grid(row=0, column=1)
        fecha.grid(row=1, column=1)
        dni.grid(row=2, column=1)
        monto.grid(row=2, column=1)

        btEnter = Button(root, text="enter", command=enter,
                         bg="Black", fg="white")

        btEnter.grid(row=50, column=70)

    def factura():

        def enter():

            caFactura.grid_forget()

            cursor.execute("Insert into empleado(idFactura,idProducto,cant,precioUni) values ('" +
                           idFactura.get() + "','" + sueldo.get() + "','" + rol.get() + "','" + nombre.get() + "'"");")
        # seinsertan los valosres, copiar y pegar con el resto de las tablas

            connection.commit()

            btEnter.grid_forget()

            root.destroy()

        btTablas.grid_forget()

        Label(caFactura, text='idFactura').grid(row=0)
        Label(caFactura, text='idProducto').grid(row=1)
        Label(caFactura, text='cant').grid(row=2)
        Label(caFactura, text='precioUni').grid(row=3)

        idFactura = Entry(caFactura)
        idProducto = Entry(caFactura)
        cant = Entry(caFactura)
        precioUni = Entry(caFactura)

        idFactura.grid(row=0, column=1)
        idProducto.grid(row=1, column=1)
        cant.grid(row=2, column=1)
        precioUni.grid(row=3, column=1)

        btEnter = Button(root, text="enter", command=enter,
                         bg="Black", fg="white")

        btEnter.grid(row=50, column=70)

    btIngreVer.grid_forget()

    btEmple = Button(btTablas, text="Empleado",
                     command=empleado, bg="Black", fg="white")

    btEmple.grid(column=10, row=10)

    btIngr = Button(btTablas, text="Ingrediente",
                    command=ingrediente, bg="Black", fg="white")

    btIngr.grid(column=20, row=10)

    btProdIngr = Button(btTablas, text="Producto\nIngrediente",
                        command=prodIngr, bg="Black", fg="white")

    btProdIngr.grid(column=30, row=10)

    btVenta = Button(btTablas, text="Venta",
                     command=venta, bg="Black", fg="white")

    btVenta.grid(column=50, row=10)

    btFactura = Button(btTablas, text="Factura",
                       command=factura, bg="Black", fg="white")

    btFactura.grid(column=60, row=10)


def ver():

    def empleado():

        btTablas.grid_forget()

        cursor.execute("SELECT * FROM empleado")

        rows = cursor.fetchall()

        texto = Text(root)

        texto.insert(END, "DNI SUELDO ROL NOMBRE DESCUENTO\n\n")

        for i in rows:
            texto.insert(END, i["dni"])

            texto.insert(END, ' ')

            texto.insert(END, i["sueldo"])

            texto.insert(END, ' ')

            texto.insert(END, i["rol"])

            texto.insert(END, ' ')

            texto.insert(END, i["nombre"])

            texto.insert(END, ' ')

            texto.insert(END, i["descuento"])

            texto.insert(END, '\n\n')

        texto.grid(column=0, row=0)

        btSalir = Button(root, text="Salir",
                         command=root.destroy, bg="Black", fg="white")

        btSalir.grid(column=1, row=1)

        btSalir.place(x=100, y=400)

    def ingrediente():

        btTablas.grid_forget()

        cursor.execute("SELECT * FROM ingrediente")

        rows = cursor.fetchall()

        texto = Text(root)

        texto.insert(END, "idIngr nombre stock unidad\n\n")

        for i in rows:
            texto.insert(END, i["idIngr"])

            texto.insert(END, ' ')

            texto.insert(END, i["nombre"])

            texto.insert(END, ' ')

            texto.insert(END, i["stock"])

            texto.insert(END, ' ')

            texto.insert(END, i["unidad"])

            texto.insert(END, '\n\n')

        texto.grid(column=0, row=0)

        btSalir = Button(root, text="Salir",
                         command=root.destroy, bg="Black", fg="white")

        btSalir.grid(column=1, row=1)

        btSalir.place(x=100, y=400)

    def prodIngr():

        btTablas.grid_forget()

        cursor.execute("SELECT * FROM producto_ingrediente")

        rows = cursor.fetchall()

        texto = Text(root)

        texto.insert(END, "idProducto idIngr cant\n\n")

        for i in rows:
            texto.insert(END, i["idProducto"])

            texto.insert(END, ' ')

            texto.insert(END, i["idIngr"])

            texto.insert(END, ' ')

            texto.insert(END, i["cant"])

            texto.insert(END, '\n\n')

        texto.grid(column=0, row=0)

        btSalir = Button(root, text="Salir",
                         command=root.destroy, bg="Black", fg="white")

        btSalir.grid(column=1, row=1)

        btSalir.place(x=100, y=400)

    def venta():

        btTablas.grid_forget()

        cursor.execute("SELECT * FROM venta")

        rows = cursor.fetchall()

        texto = Text(root)

        texto.insert(END, "idIngr nombre stock unidad\n\n")

        for i in rows:
            texto.insert(END, i["idVenta"])

            texto.insert(END, ' ')

            texto.insert(END, i["fecha"])

            texto.insert(END, ' ')

            texto.insert(END, i["dni"])

            texto.insert(END, ' ')

            texto.insert(END, i["monto"])

            texto.insert(END, '\n\n')

        texto.grid(column=0, row=0)

        btSalir = Button(root, text="Salir",
                         command=root.destroy, bg="Black", fg="white")

        btSalir.grid(column=1, row=1)

        btSalir.place(x=100, y=400)

    def producto():

        btTablas.grid_forget()

        cursor.execute("SELECT * FROM producto")

        rows = cursor.fetchall()

        texto = Text(root)

        texto.insert(END, "idFactura idProducto cant precioUni\n\n")

        for i in rows:
            texto.insert(END, i["idFactura"])

            texto.insert(END, ' ')

            texto.insert(END, i["idProducto"])

            texto.insert(END, ' ')

            texto.insert(END, i["cant"])

            texto.insert(END, ' ')

            texto.insert(END, i["precioUni"])

            texto.insert(END, '\n\n')

        texto.grid(column=0, row=0)

        btSalir = Button(root, text="Salir",
                         command=root.destroy, bg="Black", fg="white")

        btSalir.grid(column=1, row=1)

        btSalir.place(x=100, y=400)

    btIngreVer.grid_forget()

    btEmple = Button(btTablas, text="Empleado",
                     command=empleado, bg="Black", fg="white")

    btEmple.grid(column=10, row=10)

    btIngr = Button(btTablas, text="Ingrediente",
                    command=ingrediente, bg="Black", fg="white")

    btIngr.grid(column=20, row=10)

    btProdIngr = Button(btTablas, text="Producto\nIngrediente",
                        command=prodIngr, bg="Black", fg="white")

    btProdIngr.grid(column=30, row=10)

    btVenta = Button(btTablas, text="Venta",
                     command=venta, bg="Black", fg="white")

    btVenta.grid(column=50, row=10)

    btFactura = Button(btTablas, text="Factura",
                       command=factura, bg="Black", fg="white")

    btFactura.grid(column=60, row=10)


def ventHoy():
    btIngreVer.grid_forget()

    cursor.execute("select * from venta where day(fecha)=day(now());")

    rows = cursor.fetchall()

    texto = Text(root)

    texto.insert(END, "VENTAS DE HOY\n\n")

    for i in rows:
        texto.insert(END, i)

        texto.insert(END, ' ')

        texto.insert(END, '\n\n')

    texto.grid(column=0, row=0)

    btSalir = Button(root, text="Salir", command=root.destroy,
                     bg="Black", fg="white")

    btSalir.grid(column=1, row=1)

    btSalir.place(x=100, y=400)


def mayPostre():
    btIngreVer.grid_forget()

    cursor.execute(
        "select max(cant),nombre P from factura F join producto P on P.idProducto = F.idProducto;")

    rows = cursor.fetchall()

    texto = Text(root)

    texto.insert(END, "Mayor postre\n\n")

    for i in rows:
        texto.insert(END, i)

        texto.insert(END, ' ')

        texto.insert(END, '\n\n')

    texto.grid(column=0, row=0)

    btSalir = Button(root, text="Salir", command=root.destroy,
                     bg="Black", fg="white")

    btSalir.grid(column=1, row=1)

    btSalir.place(x=100, y=400)


# Connect to the database
connection = pymysql.connect(host='localhost',

                             user='root',
                             password='',
                             db='panaderia',
                             cursorclass=pymysql.cursors.DictCursor)

aux = 'N'


root = Tk()

root.geometry('500x500')

root.title("Panaderia del Tano")

btIngreVer = Frame(root)

btIngreVer.grid(column=0, row=0)

btTablas = Frame(root)

btTablas.grid(column=0, row=0)

caEmple = Frame(root)

caEmple.grid(column=0, row=0)

caIngred = Frame(root)

caIngred.grid(column=0, row=0)

caProdIngred = Frame(root)

caProdIngred.grid(column=0, row=0)

caVenta = Frame(root)

caVenta.grid(column=0, row=0)

caFactura = Frame(root)

caFactura.grid(column=0, row=0)


try:

    with connection.cursor() as cursor:
        # Read a single record
        # sql = "SELECT * FROM `users`"
        # cursor.execute(sql)
        # result = cursor.fetchone()
        # print(result)
        # Al final del while se le pide ingresar un caracter [S] O [N] y despues se le pide que quiere ver,
        # para que si no quiere ver no tenga que ingresar que quiere ver.

        btIng = Button(btIngreVer, text="Ingresar algo",
                       command=ingresar, bg="Black", fg="white")

        btIng.grid(column=1, row=1)

        btVer = Button(btIngreVer, text="Ver algo",
                       command=ver, bg="Black", fg="white")

        btVer.grid(column=2, row=1)

        btVent = Button(btIngreVer, text="Ventas de hoy",
                        command=ventHoy, bg="Black", fg="white")

        btVent.grid(column=3, row=1)

        btMayPostre = Button(btIngreVer, text="Mayor postre",
                             command=mayPostre, bg="Black", fg="white")

        btMayPostre.grid(column=4, row=1)

        root.mainloop()


finally:
    connection.close()

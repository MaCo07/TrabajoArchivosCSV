# Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.



def lectura (archivo):
    lista_productos = [] #creamos una lista en donde tendra un diccionario para cada producto

    with open ("lista_productos.txt","r") as archivo:

        for linea in archivo: #leemos cada linea del archivo

            nombre, precio, cantidad = linea.strip().split(",")#limpiamos cada linea

            producto = {
                "nombre":nombre,
                "precio":precio,
                "cantidad":cantidad
            } #a cada linea osea cada producto, y cada item le asignamos las claves para armar cada diccionario
            lista_productos.append(producto) #agregamos cada diccionario a la lista

    return lista_productos #retornamos la lista




# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

def buscar_productos(productos):

    nombre_busqueda = input("Busqueda de producto: ")

    for producto in productos: #recorremos la lista de los productos
        if producto["nombre"].lower() == nombre_busqueda.lower(): #cada producto y entrada la pasamos a minuscula
            print(producto)
            return

    print("No se encontro el producto")


# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

def guardardo (archivo,productos):

    with open(archivo,"w") as nuevo:

        for producto in productos:

            linea = f"{producto["nombre"],{producto["precio"]},{producto["cantidad"]}}\n"

            archivo.write(linea)

productos_lista = lectura("lista_productos.txt")
buscar_productos(productos_lista)
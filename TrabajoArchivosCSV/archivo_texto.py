# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad



producto_1 = "Gaseosa,2500,150\n"
producto_2 = "Mortadela,300,300\n"
producto_3 = "Fideos,1500,200\n"

with open ("lista_productos.txt","w") as lista:

    lista.write(producto_1)
    lista.write(producto_2)
    lista.write(producto_3)

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:

# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("lista_productos.txt","r") as lista_productos:

    for linea in lista_productos:

        lista = linea.strip().split(",") #limpiamos cada linea, separamos cada una de estas en base a la coma

        # resultado = "|".join(lista)

        print(f"Producto: {lista[0]} | Precio: ${lista[1]} | Cantidad: {lista[2]}") #mostramos cada item de acuerdo

        #al indice de cada lista creada


# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

print("-------------- Agregar otro producto -----------------")

with open("lista_productos.txt","a") as archivo:

    producto = []

    nombre = input("Nombre del producto: ")
    precio = input("Precio del producto: ")
    cantidad = input("Cantidad de stock: ")

    producto.append(nombre+",")
    producto.append(precio+",")
    producto.append(cantidad)

    archivo.writelines(producto)
    



with open("lista_productos.txt","r") as lista_productos:

    for linea in lista_productos:

        lista = linea.strip().split(",") #limpiamos cada linea, separamos cada una de estas en base a la coma

        # resultado = "|".join(lista)

        print(f"Producto: {lista[0]} | Precio: ${lista[1]} | Cantidad: {lista[2]}") #mostramos cada item de acuerdo

        #al indice de cada lista creada
    
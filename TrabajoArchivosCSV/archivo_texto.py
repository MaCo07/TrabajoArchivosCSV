# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

#Este lo creamos para hacer el archivo de texto, lo comentamos ya que al inicar cada vez el programa
#se nos borra cada vez que agregamos mas cosas por el metodo "w"

# producto_1 = "Gaseosa,2500,150\n"
# producto_2 = "Mortadela,300,300\n"
# producto_3 = "Fideos,1500,200\n"

# with open ("lista_productos.txt","w") as lista:

#     lista.write(producto_1)
#     lista.write(producto_2)
#     lista.write(producto_3)

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:

# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

def mostrar_productos(archivo):

    with open(archivo,"r") as productos:

        for linea in productos:

            nombre, precio, cantidad = linea.strip().split(",") #tomamos cada item en la lista y lo asignamos a una variable
            #a su vez eliminamos cada espacio en blanco

            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}") 



# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

def agregar_producto(archivo_productos):

    with open(archivo_productos,"a") as archivo: #usamos metodo append ("a")


        nombre = input("Nombre del producto: ")
        precio = input("Precio del producto: ")
        cantidad = input("Cantidad de stock: ")

        archivo.writelines(f"{nombre},{precio},{cantidad}\n") #escribimos las lineas de una vez


while True:
    print("--- Menu de Gestion ---")
    print("1 - Agregar mas Productos")
    print("2 - Mostrar la lista de Productos")
    print("3 - Cerrar programa")

    opcion = input("Elegi tu Opcion: ")

    if opcion == "1":
        agregar_producto("lista_productos.txt")
        print("Producto Agregado con exito")
    elif opcion == "2":
        print("\n----- Catalogo de Productos -----")
        mostrar_productos("lista_productos.txt")
    elif opcion == "3":
        print("Cerrando programa")
        break
    else:
        print("Opcion invalida, volve a intentar")



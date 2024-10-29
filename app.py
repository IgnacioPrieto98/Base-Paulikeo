import mysql.connector
from datetime import datetime, timedelta

# Conexión a la base de datos
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='Gestor'
    )

# Funciones de Socios
def crear_socio(nombre, apellido, dni, telefono, email):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO Socios (Nombre, Apellido, DNI, Telefono, Email) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (nombre, apellido, dni, telefono, email))

    print("/n Comprobando datos /n")

    if control_errores (nombre, apellido, dni, telefono, email):
        conexion.commit()

    cursor.close()
    conexion.close()

def control_errores (nombre, apellido, dni, telefono, email):
    if isinstance(nombre, str) and nombre.isalpha() ==0 :
        print("El nombre ingresado NO es válido")
    elif len(dni) != 8 or not dni.isdigit():
        print("El DNI debe ser un número de 8 dígitos.")
    else :
        return True
    
def actualizar_socio(id_socio, nombre, apellido, dni, telefono, email):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Socios SET Nombre = %s, Apellido = %s, DNI = %s, Telefono = %s, Email = %s WHERE ID_Socio = %s"
    cursor.execute(sql, (nombre, apellido, dni, telefono, email, id_socio))
    conexion.commit()
    cursor.close()
    conexion.close()

def borrar_socio(id_socio):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Socios SET Estado = 0 WHERE ID_Socio = %s"
    cursor.execute(sql, (id_socio,))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_socios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Socios WHERE Estado = 1")
    socios = cursor.fetchall()
    if not socios:
        print("No hay socios activos.")
    else:
        for (id_socio, nombre, apellido, dni, telefono, email, creado_el, actualizado_el, estado) in socios:
            print(f"ID: {id_socio}, Nombre: {nombre}, Apellido: {apellido}, DNI: {dni}, Teléfono: {telefono}, Email: {email}, Estado: {'Activo' if estado == 1 else 'Inactivo'}")
    cursor.close()
    conexion.close()

# Funciones de Géneros
def agregar_genero(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO Generos (Genero) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    conexion.commit()
    cursor.close()
    conexion.close()

def actualizar_genero(id_genero, nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Generos SET Genero = %s WHERE ID_Genero = %s"
    cursor.execute(sql, (nombre, id_genero))
    conexion.commit()
    cursor.close()
    conexion.close()

def borrar_genero(id_genero):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Generos SET Estado = 0 WHERE ID_Genero = %s"
    cursor.execute(sql, (id_genero,))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_generos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Generos")
    for (id_genero, nombre) in cursor.fetchall():
        print(f"ID: {id_genero}, Género: {nombre}")
    cursor.close()
    conexion.close()

# Funciones de Libros
def agregar_libro(nombre_libro, autor, fecha_lanzamiento, id_genero):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO Libros (Nombre_Libro, Autor, Fecha_Lanzamiento, ID_Genero) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre_libro, autor, fecha_lanzamiento, id_genero))
    conexion.commit()
    cursor.close()
    conexion.close()

def actualizar_libro(id_libro, nombre_libro, autor, fecha_lanzamiento, id_genero):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Libros SET Nombre_Libro = %s, Autor = %s, Fecha_Lanzamiento = %s, ID_Genero = %s WHERE ID_Libro = %s"
    cursor.execute(sql, (nombre_libro, autor, fecha_lanzamiento, id_genero, id_libro))
    conexion.commit()
    cursor.close()
    conexion.close()

def borrar_libro(id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Libros SET Estado = 0 WHERE ID_Libro = %s"
    cursor.execute(sql, (id_libro,))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_libros():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Libros WHERE Estado = 1")
    for (id_libro, nombre_libro, autor, fecha_lanzamiento, creado_el, actualizado_el, estado, id_genero) in cursor.fetchall():
        print(f"ID: {id_libro}, Título: {nombre_libro}, Autor: {autor}, Fecha de Lanzamiento: {fecha_lanzamiento}, Género ID: {id_genero}, Estado: {'Activo' if estado == 1 else 'Inactivo'}")
    cursor.close()
    conexion.close()

# Funciones de Préstamos
def crear_prestamo(id_libro, id_socio):
    conexion = conectar()
    cursor = conexion.cursor()
    
    fecha_prestamo = datetime.now().date()
    fecha_devolucion = fecha_prestamo + timedelta(days=7)
    
    sql = "INSERT INTO Prestamos (Fecha_Prestamo, Fecha_Devolucion, ID_Libro, ID_Socio) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (fecha_prestamo, fecha_devolucion, id_libro, id_socio))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Préstamo creado exitosamente.")

def listar_prestamos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Prestamos")
    for (fecha_prestamo, fecha_devolucion, id_libro, id_socio) in cursor.fetchall():
        print(f"Fecha de Préstamo: {fecha_prestamo}, Fecha de Devolución: {fecha_devolucion}, ID Libro: {id_libro}, ID Socio: {id_socio}")
    cursor.close()
    conexion.close()

# Función para verificar si se puede prestar
def puede_prestar(id_socio, id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Verificar el estado del socio
    cursor.execute("SELECT Estado FROM Socios WHERE ID_Socio = %s", (id_socio,))
    socio = cursor.fetchone()
    
    # Verificar el estado del libro
    cursor.execute("SELECT Estado FROM Libros WHERE ID_Libro = %s", (id_libro,))
    libro = cursor.fetchone()
    
    cursor.close()
    conexion.close()
    
    # Validar estados
    if socio and socio[0] == 1 and libro and libro[0] == 1:
        return True
    return False

# Menú de la aplicación
def menu():
    while True:
        print("\n--- Menú de Biblioteca ---")
        print("1. Crear Socio")
        print("2. Actualizar Socio")
        print("3. Borrar Socio")
        print("4. Listar Socios")
        print("5. Agregar Género")
        print("6. Actualizar Género")
        print("7. Borrar Género")
        print("8. Listar Géneros")
        print("9. Agregar Libro")
        print("10. Actualizar Libro")
        print("11. Borrar Libro")
        print("12. Listar Libros")
        print("13. Crear Préstamo")
        print("14. Listar Préstamos")
        print("15. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            crear_socio(nombre, apellido, dni, telefono, email)
        elif opcion == '2':
            id_socio = int(input("ID del Socio: "))
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            dni = input("Nuevo DNI: ")
            telefono = input("Nuevo Teléfono: ")
            email = input("Nuevo Email: ")
            actualizar_socio(id_socio, nombre, apellido, dni, telefono, email)
        elif opcion == '3':
            id_socio = int(input("ID del Socio: "))
            borrar_socio(id_socio)
        elif opcion == '4':
            listar_socios()
        elif opcion == '5':
            nombre = input("Nombre del Género: ")
            agregar_genero(nombre)
        elif opcion == '6':
            id_genero = int(input("ID del Género: "))
            nombre = input("Nuevo Nombre: ")
            actualizar_genero(id_genero, nombre)
        elif opcion == '7':
            id_genero = int(input("ID del Género: "))
            borrar_genero(id_genero)
        elif opcion == '8':
            listar_generos()
        elif opcion == '9':
            nombre_libro = input("Título del Libro: ")
            autor = input("Autor: ")
            fecha_lanzamiento = input("Fecha de Lanzamiento (YYYY-MM-DD): ")
            id_genero = int(input("ID del Género: "))
            agregar_libro(nombre_libro, autor, fecha_lanzamiento, id_genero)
        elif opcion == '10':
            id_libro = int(input("ID del Libro: "))
            nombre_libro = input("Nuevo Título: ")
            autor = input("Nuevo Autor: ")
            fecha_lanzamiento = input("Nueva Fecha de Lanzamiento (YYYY-MM-DD): ")
            id_genero = int(input("Nuevo ID del Género: "))
            actualizar_libro(id_libro, nombre_libro, autor, fecha_lanzamiento, id_genero)
        elif opcion == '11':
            id_libro = int(input("ID del Libro: "))
            borrar_libro(id_libro)
        elif opcion == '12':
            listar_libros()
        elif opcion == '13':
            id_libro = int(input("ID del Libro: "))
            id_socio = int(input("ID del Socio: "))
            if puede_prestar(id_socio, id_libro):
                crear_prestamo(id_libro, id_socio)
            else:
                print("No se puede prestar el libro.")
        elif opcion == '14':
            listar_prestamos()
        elif opcion == '15':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
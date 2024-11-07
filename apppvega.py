import mysql.connector
from datetime import datetime, timedelta
import os

# Mysql
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='Gestor2'
    )

# creacion tablas

def tablas():
    conexion = conectar()
    cursor = conexion.cursor()
    
    tabla_socios = """
    CREATE TABLE IF NOT EXISTS Socios(
    ID_Socio int not null UNIQUE auto_increment PRIMARY KEY,
    Nombre VARCHAR(255),
    Apellido VARCHAR(255),
    DNI VARCHAR(8),
    Telefono VARCHAR(16),
    Email VARCHAR(60),
    Creado_el TIMESTAMP DEFAULT NOW(),
    Actualizado_el TIMESTAMP DEFAULT NOW(),
    Estado tinyint DEFAULT 1
    );
    """

    cursor.execute(tabla_socios)
    print("Tabla 'Socios' creada.")
    
    tabla_generos="""
    CREATE TABLE IF NOT EXISTS Generos(
    Genero VARCHAR(80) not null,
    ID_Genero INT not null auto_increment PRIMARY KEY
    );"""
    
    cursor.execute(tabla_generos)
    print("Tabla 'Generos' creada.")
    
    tabla_libros="""
    CREATE TABLE IF NOT EXISTS Libros(
    Nombre_Libro VARCHAR(255) NOT NULL,
    ID_Libro int not null auto_increment UNIQUE PRIMARY KEY,
    Autor VARCHAR(255) NOT NULL,
    Fecha_Lanzamiento DATE,
    Creado_el TIMESTAMP DEFAULT now(),
    Actualizado_el TIMESTAMP DEFAULT now(),
    Estado tinyint DEFAULT 1,
    ID_Genero INT,
    Disponibilidad tinyint DEFAULT '1',
    FOREIGN KEY(ID_Genero) REFERENCES generos(ID_Genero)
    );
    """

    cursor.execute(tabla_libros)
    print("Tabla 'Libros' creada.")

    tabla_prestamos="""CREATE TABLE IF NOT EXISTS Prestamos(
    Fecha_Prestamo DATE,
    Fecha_Devolucion_Estimada DATE,
    Fecha_Devolucion_Real DATE,
    ID_Libro int,
    ID_Socio int,
    ID_Prestamo int not null auto_increment primary key,
    FOREIGN KEY(ID_Libro) REFERENCES libros(ID_Libro),
    FOREIGN KEY(ID_Socio) REFERENCES socios(ID_Socio)
    );"""

    cursor.execute(tabla_prestamos)
    print("Tabla 'Prestamos' creada.")

    cursor.close()
    conexion.close()
    


# region (SOCIOS)

# Socios
def crear_socio(nombre, apellido, dni, telefono, email):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO Socios (Nombre, Apellido, DNI, Telefono, Email) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (nombre, apellido, dni, telefono, email))

    conexion.commit()

    cursor.close()
    conexion.close()
    
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

# endregion 

# region (GENERO)

# Géneros
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
    for (nombre, id_genero) in cursor.fetchall():
        print(f"ID: {id_genero}, Género: {nombre}")
    cursor.close()
    conexion.close()

# endregion

# region (LIBROS)
# Libros
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
    for (nombre_libro, id_libro, autor, fecha_lanzamiento, creado_el, actualizado_el, estado, id_genero, Disponibilidad) in cursor.fetchall():
        print(f"ID: {id_libro}, Título: {nombre_libro}, Autor: {autor}, Fecha de Lanzamiento: {fecha_lanzamiento}, Género ID: {id_genero}, Estado: {'Activo' if estado == 1 else 'Inactivo'}")
    cursor.close()
    conexion.close()

#endregion

# region (PRESTAMOS)

# Préstamos
def crear_prestamo(id_libro, id_socio):
    conexion = conectar()
    cursor = conexion.cursor()
    
    fecha_prestamo = datetime.now().date()
    fecha_devolucion_estimada = fecha_prestamo + timedelta(days=7)
    
    sql = "INSERT INTO Prestamos (Fecha_Prestamo, fecha_devolucion_estimada, ID_Libro, ID_Socio) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (fecha_prestamo, fecha_devolucion_estimada, id_libro, id_socio))

    sql2 = "UPDATE Libros SET Disponibilidad = 0 WHERE ID_Libro = %s"
    cursor.execute(sql2, (id_libro,))

    conexion.commit()
    cursor.close()
    conexion.close()
    print("Préstamo creado exitosamente.")

def listar_prestamos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Prestamos")
    for (fecha_prestamo, fecha_devolucion_estimada,fecha_devolucion_real, id_libro, id_socio, id_prestamo) in cursor.fetchall():
        print(f"Fecha de Préstamo: {fecha_prestamo}, Fecha de Devolución Estimada: {fecha_devolucion_estimada}, ID Libro: {id_libro}, ID Socio: {id_socio}")
    cursor.close()
    conexion.close()

# Si se puede prestar
def puede_prestar(id_socio, id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Estado del socio
    cursor.execute("SELECT Estado FROM Socios WHERE ID_Socio = %s", (id_socio,))
    socio = cursor.fetchone()
    
    # Estado del libro
    cursor.execute("SELECT Estado FROM Libros WHERE ID_Libro = %s", (id_libro,))
    libro = cursor.fetchone()
    
    # Disponibilidad libro
    cursor.execute("SELECT Disponibilidad FROM Libros WHERE ID_Libro = %s", (id_libro,))
    disponibilidad = cursor.fetchone()

    cursor.close()
    conexion.close()
    
    # Estados
    if socio and socio[0] == 1 and libro and libro[0] == 1 and disponibilidad[0]== 1:
        return True
    return False

def actualizar_prestamo(id_libro, id_socio, id_prestamo):
    conexion = conectar()
    cursor = conexion.cursor()

    Fecha_Devolucion_Real = datetime.now().date()
    
    cursor.execute("SELECT Fecha_Devolucion_Estimada FROM Prestamos WHERE ID_Prestamo = %s" , (id_prestamo,))
    Fecha_Devolucion_Estimada = cursor.fetchone()

    sql2 = "UPDATE Libros SET Disponibilidad = 1 WHERE ID_Libro = %s"
    cursor.execute(sql2, (id_libro,))
    
    sql_Fecha="UPDATE Prestamos SET Fecha_Devolucion_Real = %s WHERE ID_Prestamo=%s" 
    cursor.execute(sql_Fecha, (Fecha_Devolucion_Real,id_prestamo))

    if (Fecha_Devolucion_Real > Fecha_Devolucion_Estimada[0]):
        sql_Estado= "UPDATE Socios SET Estado = 0 WHERE ID_Socio = %s"
        cursor.execute(sql_Estado, (id_socio,))
        os.system('cls')    
        print("\n Entrega fuera de término \n")   
    else:
        os.system('cls')
        print("\n Devolución en tiempo \n")   

    conexion.commit()
    cursor.close()
    conexion.close()

# endregion

# region (MENU)
# Menú
def menu():
    while True:
        print("\n--- Menu Principal ---\n")
        print("1. Socios")
        print("2. Prestamos") 
        print("3. Libros")
        print("4. Generos")
        print("5. Salir") 
        opcion = input("\n Seleccione una opción:")
        os.system('cls')
        
#region (1. Socios)
        if(opcion == '1'):
            print("\n--- Menu de socios ---\n")

            print("1. Crear Socio")
            print("2. Actualizar Socio")
            print("3. Borrar Socio")
            print("4. Listar Socios")
            print("5. Volver")

            opcion2 = input("\nSeleccione una opción: ")

            if opcion2 == '1':
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                dni = input("DNI: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                
                print(" \n Está seguro de realizar los cambios  \n ")
                opcion3 = input("\n Si (1) / No (0) ")
                if(opcion3 == '1'):
                    crear_socio(nombre, apellido, dni, telefono, email)
                    os.system('cls')
                    print(" \n Usuario creado con éxito  \n ")
                else:
                    os.system('cls')
                    print(" \n Usuario NO creado \n ")
                    menu()

            if opcion2 == '2':
                id_socio = int(input("ID del Socio: "))
                nombre = input("Nuevo Nombre: ")
                apellido = input("Nuevo Apellido: ")
                dni = input("Nuevo DNI: ")
                telefono = input("Nuevo Teléfono: ")
                email = input("Nuevo Email: ")
                
                print(" \n Está seguro de realizar los cambios  \n ")
                opcion3 = input("\n Si (1) / No (0) ")
                if(opcion3 == '1'):
                    actualizar_socio(id_socio, nombre, apellido, dni, telefono, email) 
                    os.system('cls')
                    print(" \n Usuario actualizado con éxito \n ")
                else:
                    os.system('cls')
                    print(" \n Usuario NO actualizado \n ")
                    menu() 

            if opcion2 == '3':
                id_socio = int(input("ID del Socio: "))

                print(" \n Está seguro de realizar los cambios  \n ")
                opcion3 = input("\n Si (1) / No (0) ")
                if(opcion3 == '1'):
                    borrar_socio(id_socio)
                    os.system('cls')
                    print(" \n Usuario borrado con éxito  \n ")
                else:
                    os.system('cls')
                    print(" \n Usuario NO borrado  \n ")
                    menu()

            if opcion2 == '4':
                listar_socios()
                opcion3 = input("\n presionar enter para volver")
                os.system('cls')
                menu()

            if(opcion2 == '5'):
                os.system('cls')
                menu()
#endregion 

#region (2. Prestamos)
        if(opcion == '2'):
            print("\n--- Menu de Préstamos ---\n")

            print("1. Crear Prestamo")
            print("2. Actualizar Préstamo")
            print("3. Listar Préstamos")
            print("4. Volver")

            opcion2 = input("\n Seleccione una opción: ")

            if opcion2 == '1':
                id_libro = int(input("ID del Libro: "))
                id_socio = int(input("ID del Socio: "))

                print(" \n Está seguro de realizar los cambios  \n ")
                opcion3 = input("\n Si (1) / No (0) ")
                if(opcion3 == '1'):
                    if puede_prestar(id_socio, id_libro):
                        crear_prestamo(id_libro, id_socio)
                        os.system('cls')
                        print("\n Prestamo asignado correctamente. \n")

                    else:
                        os.system('cls')
                        print("No se puede prestar el libro.")
                else:
                    os.system('cls')
                    print("\n Prestamo NO asignado. \n")
                    menu()                

            if opcion2 == '2':
                id_libro = int(input("ID del Libro: "))
                id_socio= int(input("ID del Socio: "))
                id_prestamo = int(input("ID del Préstamo: "))

                print(" \n Está seguro de realizar los cambios  \n ")
                opcion3 = input("\n Si (1) / No (0) ")
                if(opcion3 == '1'):
                    actualizar_prestamo(id_libro, id_socio, id_prestamo)
                    print(" \n Libro devuelto  \n ")
                    menu()
                else:
                    os.system('cls')
                    print(" \n Libro NO devuelto \n ")
                    menu()

            if opcion2 == '3':
                listar_prestamos()
                opcion3 = input("\n presionar enter para volver ")
                os.system('cls')
                menu()

            if(opcion2 == '4'):
                os.system('cls')
                menu()
#endregion

#region (3. Libros)
        if(opcion == '3'):
            print("\n--- Menu de Libros ---\n")

            print("1. Agregar Libro")
            print("2. Actualizar Libro")
            print("3. Borrar Libro")
            print("4. Listar Libros")
            print("5. Volver") 

            opcion2 = input("\n Seleccione una opción: ")
            
            if opcion2 == '1':
                nombre_libro = input("Título del Libro: ")
                autor = input("Autor: ")
                fecha_lanzamiento = input("Fecha de Lanzamiento (YYYY-MM-DD): ")
                id_genero = int(input("ID del Género: "))

                print(" \n Está seguro de realizar los cambios  \n ")
                opcion3 = input("\n Si (1) / No (0) ")
                if(opcion3 == '1'):
                    agregar_libro(nombre_libro, autor, fecha_lanzamiento, id_genero)
                    os.system('cls')
                    print(" \n Libro agregado con éxito  \n ")
                else:
                    os.system('cls')
                    print(" \n Libro NO agregado  \n ")
                    menu()
                

            if opcion2 == '2':
                id_libro = int(input("ID del Libro: "))
                nombre_libro = input("Nuevo Título: ")
                autor = input("Nuevo Autor: ")
                fecha_lanzamiento = input("Nueva Fecha de Lanzamiento (YYYY-MM-DD): ")
                id_genero = int(input("Nuevo ID del Género: "))

                print(" \n Está seguro de realizar los cambios  \n ")
                opcion3 = input("\n Si (1) / No (0) ")
                if(opcion3 == '1'):
                    actualizar_libro(id_libro, nombre_libro, autor, fecha_lanzamiento, id_genero)
                    os.system('cls')
                    print("\n Libro actualizado correctamente \n ")
                else:
                    os.system('cls')
                    print("\n Libro NO actualizado \n ")
                    menu() 

            if opcion2 == '3':
                id_libro = int(input("ID del Libro: "))

                print(" \n Está seguro de realizar los cambios  \n ")
                opcion3 = input("\n Si (1) / No (0) ")
                if(opcion3 == '1'):
                    borrar_libro(id_libro)
                    os.system('cls')
                    print(" \n Libro borrado con éxito  \n ")
                else:
                    os.system('cls')
                    print(" \n Libro NO borrado \n ")
                    menu()
            
            if opcion2 == '4':
                listar_libros()
                opcion3 = input("\n presionar enter para volver \n ")
                os.system('cls')
                menu()
            
            if(opcion2 == '5'):
                os.system('cls')
                menu()

#endregion

#region (4. Géneros)
                
        if(opcion == '4'):
            print("\n--- Menu de Generos ---\n")

            print("1. Agregar Género")
            print("2. Actualizar Género")
            print("3. Borrar Género")
            print("4. Listar Géneros")
            print("5. Volver")

            opcion2 = input("\n Seleccione una opción: ")

            if opcion2 == '1':
                nombre = input("Nombre del Género: ")
                
                print(" \n Está seguro de realizar los cambios  \n ")
                opcion3 = input("\n Si (1) / No (0) ")
                if(opcion3 == '1'):
                    agregar_genero(nombre)
                    os.system('cls')
                    print(" \n Genero agregado con éxito  \n ")
                else:
                    os.system('cls')
                    print(" \n Genero NO agregado  \n ")
                    menu()

            if opcion2 == '2':
                id_genero = int(input("ID del Género: "))
                nombre = input("Nuevo Nombre: ")

                print(" \n Está seguro de realizar los cambios  \n ")
                opcion3 = input("\n Si (1) / No (0) ")
                if(opcion3 == '1'):
                    actualizar_genero(id_genero, nombre)
                    os.system('cls')
                    print(" \n Genero actualizado con éxito  \n ")
                else:
                    os.system('cls')
                    print(" \n Genero NO actualizado  \n ")
                    menu()
                

            if opcion2 == '3':
                id_genero = int(input("ID del Género: "))
                print(" \n Está seguro de realizar los cambios  \n ")
                opcion3 = input("\n Si (1) / No (0) ")
                if(opcion3 == '1'):
                    borrar_genero(id_genero)
                    os.system('cls')
                    print(" \n Genero borrado con éxito  \n ")
                else:
                    os.system('cls')
                    print(" \n Genero NO borrado  \n ")
                    menu()
                
            if opcion2 == '4':
                listar_generos()
                opcion3 = input("\n presionar enter para volver")
                os.system('cls')
                menu()
            
            if(opcion2 == '5'):
                os.system('cls')
                menu()
                
#endregion
        
        
        if(opcion == '5'):
            break
        
            
if __name__ == "__main__":
    tablas()
    menu()
#endregion

CREATE TABLE Libros(
Nombre_Libro VARCHAR(255) NOT NULL,
Autor VARCHAR(255) NOT NULL,
Fecha_Lanzamiento DATE,
ID_Genero INT,
FOREIGN KEY(ID_Genero) REFERENCES generos(ID_Genero)
);
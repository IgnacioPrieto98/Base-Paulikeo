CREATE TABLE Libros(
Nombre_Libro VARCHAR(255) NOT NULL,
Autor VARCHAR(255) NOT NULL,
Fecha_Lanzamiento DATE,
Creado_el TIMESTAMP DEFAULT now(),
Actualizado_el TIMESTAMP DEFAULT now(),
Estado tinyint DEFAULT 1,
ID_Genero INT,
FOREIGN KEY(ID_Genero) REFERENCES generos(ID_Genero)
);
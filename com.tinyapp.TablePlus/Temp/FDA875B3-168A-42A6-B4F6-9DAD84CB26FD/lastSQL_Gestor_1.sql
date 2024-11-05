CREATE TABLE Generos(
Genero VARCHAR(80) not null,
ID_Genero INT not null auto_increment PRIMARY KEY
);CREATE TABLE Prestamos(
Fecha_Prestamo DATE,
Fecha_Devolucion DATE,
Fecha_Devolucion_Estimada DATE,
Fecha_Devolucion_Real DATE,
ID_Libro int,
ID_Socio int,
FOREIGN KEY(ID_Libro) REFERENCES libros(ID_Libro),
FOREIGN KEY(ID_Socio) REFERENCES socios(ID_Socio)
);ALTER TABLE prestamos ADD COLUMN ID_Prestamo int NOT NULL AUTO_INCREMENT PRIMARY KEY;ALTER TABLE prestamos ADD COLUMN ID_Prestamo int NOT NULL AUTO_INCREMENT;
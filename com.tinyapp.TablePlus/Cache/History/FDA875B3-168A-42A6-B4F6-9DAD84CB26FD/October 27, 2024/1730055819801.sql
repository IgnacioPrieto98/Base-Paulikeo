CREATE TABLE Socios(
ID int UNIQUE auto_increment,
Nombre VARCHAR(255),
Apellido VARCHAR(255),
DNI VARCHAR(8),
Telefono VARCHAR(16),
Email VARCHAR(60),
Creado_el TIMESTAMP DEFAULT NOW(),
Actualizado_el TIMESTAMP DEFAULT NOW(),
Estado tinyint defaul 1,
PRIMARY KEY(ID)
);
CREATE TABLE Socios(
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
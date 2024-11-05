CREATE TABLE Socios(
ID int not null unique auto_increment PRIMARY KEY,
nombre VARCHAR(255) NOT NULL,
apellido VARCHAR(255) NOT NULL,
dni VARCHAR(8),
telefono VARCHAR(16),
email VARCHAR(255),
creado_el TIMESTAMP DEFAULT now(),
actualizado_el TIMESTAMP DEFAULT now(),
estado tinyint DEFAULT 1
);
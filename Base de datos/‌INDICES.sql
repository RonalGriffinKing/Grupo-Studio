-- INDICES EN MSQL
-- indice clave primaria
-- Cada valor es unico 


use indices_prueba;
 
 
 
create table Ejemplo(
	dni varchar(10),
    nombre varchar(30),
    apellido varchar(50),
    edad int,
    primary key(dni)
);

-- Otra forma de añadir PRIMARY KEY DESPUES DE CREAR
-- La tabla
ALTER TABLE EJEMPLO ADD PRIMARY KEY(dni);

-- AGREGAR PRIMARY PRIMARY KEY DESPUES DE CREAR LA TABLA PUEDE SER COMPUESTA ENTONCES 
AlTER TABLE EJEMPLO ADD PRIMARY KEY(NOMBRE,APELLIDO);


-- Indice ordinario Permiten Duplicados PUEDE REPETIRSE NO ES UNICO
CREATE INDEX indice_ordi ON EJEMPLO(APELLIDO);

-- Indice UNICO -- NO Duplicados - - SI NULL

CREATE UNIQUE INDEX indice_unico ON EJEMPLO(NOMBRE);

-- BORRAR UN INDICE
DROP INDEX indice_unico ON EJEMPLO;

-- INDICE COMPUESTO -- MULTIPLES COLUMNAS -- SI NULL
CREATE UNIQUE INDEX indice_compuesto ON EJEMPLO(NOMBRE,APELLIDO);

ALTER TABLE EJEMPLO DROP PRIMARY KEY;







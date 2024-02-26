-- Eliminar la base de datos APPLE si existe
DROP DATABASE IF EXISTS APPLE;

-- Crear la base de datos APPLE
CREATE DATABASE APPLE;

-- Usar la base de datos APPLE
USE APPLE;

-- Crear una tabla MODELOS
CREATE TABLE MODELOS (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Modelo VARCHAR(32),
    Anio_lanzamiento INT,
    Proveedor VARCHAR(50)
);

-- Insertar registros en la tabla MODELOS
INSERT INTO MODELOS (Modelo, Anio_lanzamiento, Proveedor) VALUES 
('iPhone 11', 2019, 'Apple Inc.'),
('iPhone 12', 2020, 'Apple Inc.'),
('iPhone 13', 2021, 'Apple Inc.');

-- Agregar una nueva columna a la tabla MODELOS
ALTER TABLE MODELOS
ADD COLUMN Estado VARCHAR(20);

-- Cambiar el nombre de la tabla MODELOS a MODELOS_APPLE
ALTER TABLE MODELOS
RENAME TO MODELOS_APPLE;

-- Cambiar el nombre de la columna Modelo a Modelo_nombre en la tabla MODELOS_APPLE
ALTER TABLE MODELOS_APPLE
CHANGE COLUMN Modelo Modelo_nombre VARCHAR(50);

-- Cambiar el tipo de datos de la columna Anio_lanzamiento a YEAR en la tabla MODELOS_APPLE
ALTER TABLE MODELOS_APPLE
MODIFY COLUMN Anio_lanzamiento YEAR;

-- Eliminar la columna Proveedor de la tabla MODELOS_APPLE
ALTER TABLE MODELOS_APPLE
DROP COLUMN Proveedor;

-- Crear una tabla IPHONES
CREATE TABLE IPHONES (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Modelo VARCHAR(32),
    Nombre VARCHAR(32),
    precio FLOAT,
    id_modelo INT UNSIGNED,
    Color VARCHAR(20),
    FOREIGN KEY (id_modelo) REFERENCES MODELOS_APPLE(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- Insertar registros en la tabla IPHONES
INSERT INTO IPHONES (Modelo, Nombre, precio, id_modelo, Color) VALUES
('iPhone 11', 'iPhone 11 Standard', 699.99, 1, 'Negro'),
('iPhone 11', 'iPhone 11 Pro', 999.99, 1, 'Gris Espacial'),
('iPhone 12', 'iPhone 12 Mini', 699.99, 2, 'Blanco'),
('iPhone 12', 'iPhone 12', 799.99, 2, 'Negro'),
('iPhone 13', 'iPhone 13', 799.99, 3, 'Azul');

-- Consultas SELECT básicas para la tabla MODELOS_APPLE
SELECT Modelo_nombre FROM MODELOS_APPLE;
SELECT Modelo_nombre, Anio_lanzamiento FROM MODELOS_APPLE;

-- Consultas SELECT básicas para la tabla IPHONES
SELECT Modelo FROM IPHONES;
SELECT Modelo, Nombre, precio FROM IPHONES;

-- Campos calculados (utilizando la tabla IPHONES)
SELECT Nombre, precio, precio * 1.15 AS precio_con_impuesto FROM IPHONES;

-- Funciones MySQL en el SELECT (utilizando la tabla IPHONES)
SELECT CONCAT(Modelo, ' - ', Nombre) AS descripcion FROM IPHONES;

-- Modificadores ALL, DISTINCT y DISTINCTROW (utilizando la tabla MODELOS_APPLE)
SELECT DISTINCT Modelo_nombre FROM MODELOS_APPLE;
SELECT DISTINCT Modelo_nombre, Anio_lanzamiento FROM MODELOS_APPLE;

-- Clausula LIMIT (utilizando la tabla MODELOS_APPLE)
SELECT * FROM MODELOS_APPLE LIMIT 5;

-- Operadores IS y IS NOT (utilizando la tabla MODELOS_APPLE)
SELECT * FROM MODELOS_APPLE WHERE Estado IS NULL;

-- Consultas LIKE (ejemplos utilizando la tabla MODELOS_APPLE)
SELECT * FROM MODELOS_APPLE WHERE Modelo_nombre LIKE '%iPhone%';

-- Actualización de Registros con UPDATE (ejemplo utilizando la tabla MODELOS_APPLE)
UPDATE MODELOS_APPLE SET Anio_lanzamiento = 2023 WHERE Modelo_nombre = 'iPhone 13';

-- Eliminación de Registros con DELETE (ejemplo utilizando la tabla MODELOS_APPLE)
DELETE FROM MODELOS_APPLE WHERE Modelo_nombre = 'iPhone 11';

-- Crear un usuario con contraseña genérica
CREATE USER 'nuevo_usuario'@'localhost' IDENTIFIED BY 'contraseña_generica';

-- Asignar privilegios al usuario en la base de datos APPLE
GRANT ALL PRIVILEGES ON APPLE.* TO 'nuevo_usuario'@'localhost';

-- Refrescar los privilegios para que surtan efecto
FLUSH PRIVILEGES;


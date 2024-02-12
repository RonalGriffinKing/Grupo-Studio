SELECT *
FROM alumno
where apellido1 = "Martinez";
SELECT *
from alumno
where id = 9;
SELECT nombre,
    fecha_nacimiento
FROM alumno
WHERE fecha_nacimiento > '1997/01/01';
--TODOS LOS ALUMNOS CON ID 1
SELECT *
FROM alumno
WHERE id = 1;
--Todos los alumnos con telefono
SELECT *
from alumno
where teléfono = '692735409';
--DEVUELVE TODOS LOS ALUMNOS REPETIDORES
SELECT *
FROM alumno
WHERE es_repetidor = "si";
--Devuelve todos los que noestan repitiendo
SELECT *
FROM alumno
WHERE es_repetidor = "no";
--Todos los alumnos nacidos antes del 1 de enero del 1993

SELECT  * from alumno where fecha_nacimiento<='1993/01/01';
--Todos los nacidos despues del 1 de nero del 1994
SELECT  * from alumno where fecha_nacimiento>='1994/01/01';
--Todos los nacidos despues del 1 de enero del 1994 y que no repitan
SELECT  * from alumno where fecha_nacimiento>='1994/01/01' and es_repetidor="no";

--Todos los alumnos que nacieron en 1998

--Todos los alumnos que no ncieron en 1998

 












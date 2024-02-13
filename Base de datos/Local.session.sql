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


--Obtener todos los datos de los alumnos cuyo primer nomre es martinez, sanchez, o dominguez
SELECT * from alumno where apellido1 in("Sanchez","Martinez","Dominguez")
 

--Like

SELECT * from alumno where apellido1 like "M%";
SELECT * from alumno where apellido1 not like "M%";

--#obtener todos los alumnos que tengan en su nombre una a
SELECT * from alumno where apellido1 like "%a%";

SELECT * from alumno where apellido1  like "%a%m%c%";


-- los nombre de los alnumbos que tengan en su nombre 5 caracteres
SELECT nombre from alumno where nombre  like "_____";

-- Obtener todos los almnos cuya tercera letra es una N

SELECT * from alumno where nombre like "__n%";


-- Obtener todos los almnos cuya palabra tengo % 

SELECT * from alumno where nombre like "A$%BC" escape "$";



























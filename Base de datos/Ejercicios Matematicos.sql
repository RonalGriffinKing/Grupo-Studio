use tienda_2024;
select * from productos;

-- Consultas de calculo
-- Calcular el nombre de los articulos la seccion y el precio mas el 21% de iva añadido
select nombre_articulo, seccion, precio, precio*1.21 as Precio_final from tienda_2024.productos;   
-- Consultas de calculo
-- Calcular el nombre de los articulos la seccion y el precio mas el 21% de iva añadido y añadir dos decimales
select nombre_articulo, seccion, precio, truncate(precio*1.21,3) as Precio_final from tienda_2024.productos;   
-- Consultas de calculo
-- Calcular el nombre de los articulos la seccion y el precio mas el 21% de iva añadido aplicar un descuento de 3 euros  un campo nuevo
select nombre_articulo, seccion, precio, truncate(precio*1.21,3) as Precio_con_iva,precio-3 as Precio_con_descuento from tienda_2024.productos;   
-- Articulos que muestren los dias de diferencia desde la fecha de introduccion del articulo hasta el dia de hoy, cuantos dias han pasado.
select nombre_articulo, fecha as Fecha_inicial, current_date() AS Fecha_hoy,datediff(current_date(),fecha) as cantidad_dias from tienda_2024.productos;
-- Articulos que muestren los dias de diferencia desde la fehca de introduccion del artitulo hasta el dia de hoy solo de deportes cuantos dias han pasado
select nombre_articulo,seccion, fecha as Fecha_inicial, current_date() AS Fecha_hoy,datediff(current_date(),fecha) as cantidad_dias  from tienda_2024.productos where seccion="DEPORTES";



-- 1) PRECIO MEDIO DE CADA SECCION.
use tienda_2024;
select seccion, round(avg(precio),2) as precio_medio from productos group by seccion;

-- 2) PRECIO TOTAL POR PRODUCTOS POR PAIS DE ORIGEN.
use tienda_2024;
select pais_origen, sum(precio) as precio_total from productos group by pais_origen;
-- 3) PRODUCTO MAS CARO POR SECCION.
use tienda_2024;
SELECT nombre_articulo, seccion, precio FROM productos p1 WHERE precio = (SELECT MAX(precio) FROM productos p2 WHERE p1.seccion = p2.seccion
);
-- 4) PRODUCTO MAS BARATO POR PAIS DE ORIGEN.
select pais_origen,min(precio) from productos group by pais_origen;
-- 5) PARA CADA PAIS PARA CADA SECCION ARTICULO MAS BARATO.
select seccion,min(precio) from productos group by seccion;
-- 6) CONSULTA QUE MUESTRE CUENTO SUMAN LOS ARTICULOS DE LAS 
--    SECCIONES.
select seccion, sum(precio)  from productos group by seccion;
-- 7) MEDIA DE TODOS LOS ARTICULOS DE DEPORTES Y CERAMICA.
select seccion, round(avg(precio),2) as media_total  from productos where seccion="deportes" or seccion="ceramica" group by seccion;
-- 8) CUANTOS CLIENTES TENGO POR POBLACION.
select count(codigo_cliente) as Cantidad_clientes,poblacion from clientes group by poblacion;
-- 9) PRECIO DEL ARTICULO MAS CARO DE LA SECCION CONFECCION.
select seccion, max(precio) from productos where seccion="confeccion";
-- 10) NOMBRE DE LOS ARTICULOS QUE TIENEN COMO MINIMO 4 LETRAS.
select nombre_articulo, precio from productos where nombre_articulo like "____%";
-- 11) NOMBRE ARTICULOS QUE EMPIEZAN POR A SEGUIDOS DE 5 LETRAS.
select nombre_articulo, precio from productos where nombre_articulo like "A_____%";
-- 12) USAR CAMPO RESPONSABLE TABLA CLIENTE.

-- 12A) CLIENTES CON UNA M EN SU NOMBRE.
select responsable, telefono from clientes where responsable like "%M%";
-- 12B) CLIENTES CUYO NOMBRE EMPIEZA POR M.
select responsable, telefono from clientes where responsable like "M%";
-- 12C) CLIENTES CUYO NOMBRE TERMINA EN A.
select responsable, telefono from clientes where responsable like "%A";
-- 12D) CLIENTES CON NOMBRE DE MAS DE 10 LETRAS DE LONGITUD.
select responsable, telefono from clientes where responsable like "__________%";
-- 12E) CLIENTES CUYO NOMBRE TIENE UNA AS Y UNA R.
select responsable, telefono from clientes where responsable like "%AS%" and responsable like "%R%";
-- 13) PAISES QUE TENGAN 1 O MENOS ARTICULOS.
select pais_origen, count(nombre_articulo) as cantidad_artitulo from productos group by pais_origen having count(nombre_articulo)<=1;
-- 14) TODOS LOS PAISES MENOS CHINA, ESPAÑA Y USA.
select nombre_articulo, pais_origen from productos where pais_origen !="China" and pais_origen !="españa" and pais_origen !="usa";

SELECT DISTINCT nombre_articulo, pais_origen FROM productos WHERE pais_origen NOT IN ('China', 'España', 'USA');



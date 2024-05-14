#TRIGGERS

USE TIENDA_2024;

CREATE TABLE registro_productos(
	CodigoArticulo VARCHAR (4),
    NombreArticulo varchar(30),
    Precio DOUBLE,
    Insertado datetime
);



#Creacion del TRIGGER

CREATE TRIGGER Productos_AI AFTER INSERT ON PRODUCTOS FOR each row INSERT INTO REGISTRO_PRODUCTOS(CodigoArticulo,NombreArticulo,Precio,Insertado) VALUES( NEW.Codigo_Articulo,New.Nombre_Articulo,NEW.PRECIO,NOW());

DROP TRIGGER PRODUCTOS_AI;

insert into productos(codigo_articulo,nombre_articulo,precio,pais_origen) values ("AR75","PEINE",20,"CHINA");

SELECT * FROM registro_productos;
select * from productos;

#TRIGGER DE ACTUALIZACION
CREATE TABLE PRODUCTOS_ACTUALIZADOS(
ant_codigoarticulo varchar(4),
ant_nombrearticulo varchar(30),
ant_seccion varchar(10),
ant_precio double,
ant_importado tinyint,
ant_paisorigen varchar(15),
ant_fecha date,
nuevo_codigoarticulo varchar(4),
nuevo_nombrearticulo varchar(30),
nuevo_seccion varchar(10),
nuevo_precio double,
nuevo_importado tinyint,
nuevo_paisorigen varchar(15),
nuevo_fecha date,
usuario varchar(20),
momento_ejecucion datetime
);

drop trigger productos_bu;

CREATE TRIGGER PRODUCTOS_BU BEFORE UPDATE ON PRODUCTOS FOR EACH ROW INSERT INTO PRODUCTOS_ACTUALIZADOS()
VALUES(

old.codigo_articulo,
old.nombre_articulo,
old.seccion,
old.precio,
old.importado,
old.pais_origen,
old.fecha,

new.codigo_articulo,
new.nombre_articulo,
new.seccion,
new.precio,
new.importado,
new.pais_origen,
new.fecha,
current_user(),
now()
);

update productos set precio=precio+20, pais_origen="CONGO" WHERE codigo_articulo="AR07";




#TRIGGER ELIMINACION 

CREATE TABLE productos_Eliminados(
codigo_articulo varchar(4),
nombre_articulo varchar(30),
seccion varchar(15),
precio double,
pais_origen varchar(10)
);


drop trigger productos_ad;
create trigger PRODUCTOS_AD  AFTER DELETE ON PRODUCTOS FOR each row   INSERT INTO PRODUCTOS_ELIMINADOS() VALUES(
old.codigo_articulo,
old.nombre_articulo,
old.seccion,
old.precio,
old.pais_origen,
current_user(),
now()
);

delete from productos where codigo_articulo="AR75";


#Eliminado diferente
#Agregamos a la tabla los necesario spara poder guardarlo
alter table productos_eliminados add column(
	usuario varchar(20),
    fecha_borrado datetime
);



#Funcion que se utiliza en la base de datos
create procedure clientes_madrid()
select* from clientes
where poblacion="madrid";


call clientes_madrid();#LLamar a la funcion previamente creada arriba


#FUNCION CON PARAMETROS 
create procedure Actualiza_productos(nuevo_precio double,codigo varchar(4))
update productos set precio=nuevo_precio where codigo_articulo=codigo;




call actualiza_productos(60,"AR75");

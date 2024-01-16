DROP DATABASE IF EXISTS pruebas_integridad;
CREATE DATABASE pruebas_integridad;
USE pruebas_integridad;

CREATE TABLE usuarios(
id_usuario int unsigned primary key,
nombre varchar(20),
edad tinyint unsigned,
correo varchar(150)
);

CREATE TABLE curso(
id_curso int unsigned auto_increment primary key,
asignatura varchar(20) not null,
capacidad tinyint unsigned,
id_usuario int unsigned,
foreign key (id_usuario) references usuarios(id_usuario)
);


delete  from usuarios where id_usuario=1;
update usuarios set id_usuario=6,nombre="Roberto",edad=30,correo="briones459@gmail.com" where id_usuario=1;

create user "Nombre"@"ipmaquina" identified by "1234";
create user "Pepito"@"localhost" identified by "1234";
alter user "Pepito"@"localhost" identified by "Clave nueva"



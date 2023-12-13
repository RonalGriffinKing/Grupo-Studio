drop database if exists pinacoteca;
create database pinacoteca;
use pinacoteca;

create table pinacoteca(
codigo int primary key auto_increment,
nombre varchar(30),
ciudad varchar(45),
direccion varchar(100),
metros2 float
);

create table escuela(
nombre varchar(30) primary key,
pais varchar(45),
fecha_aparicion date
);

create table pintor(
nombre varchar(30) primary key,
pais varchar(45),
ciudad varchar(45),
fecha_nacimiento date,
fecha_difuncion date,
nombre_escuela varchar(30),
nombre_maestro varchar(30),
FOREIGN KEY (nombre_escuela) references escuela(nombre),
FOREIGN KEY (nombre_maestro) REFERENCES pintor(nombre)
);

create table cuadros(
nombre varchar(30) primary key,
dimensiones varchar(30),
fecha_pintado date,
tenica_utilizada varchar(20),
nombre_pintor varchar(30),
FOREIGN KEY (nombre_pintor) REFERENCES pintor(nombre) 
);

create table hecenas(
nombre varchar(30) primary key,
fecha_muerte date,
ciudad_nacimiento varchar(30),
pais varchar(30),
fecha varchar(30)
);

create table cuadros_hecenas(
codigo int primary key auto_increment,
 nombre_hecenas varchar(30),
 nombre_cuadro varchar(30),
 foreign key (nombre_hecenas) references hecenas(nombre),
 foreign key (nombre_cuadro) references cuadros(nombre)
);








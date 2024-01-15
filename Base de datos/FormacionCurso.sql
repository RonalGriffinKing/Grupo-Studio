DROP DATABASE IF EXISTS CursoFormacion;
CREATE DATABASE CursoFormacion CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
USE CursoFormacion;

CREATE TABLE Curso (
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(20) NOT NULL,
  descripcion VARCHAR(500) NOT NULL,
  duracion SMALLINT UNSIGNED NOT NULL,
  costo FLOAT(7,2) NOT NULL
);

CREATE TABLE CursoPre (
  id_CursoPre INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  id_Curso INT UNSIGNED,
  id_Curso_prerrequisito INT UNSIGNED,
  Obligatorio BOOLEAN NOT NULL,
  FOREIGN KEY (id_Curso_prerrequisito) REFERENCES Curso(id),
  FOREIGN KEY (id_Curso) REFERENCES Curso(id)
);

CREATE TABLE Empleado (
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(20) NOT NULL,
  apellido1 VARCHAR(20) NOT NULL,
  apellido2 VARCHAR(20) NOT NULL,
  telefono VARCHAR(12) NOT NULL UNIQUE,
  direccion VARCHAR(50) NOT NULL,
  tipo ENUM("Capacitado","No capacitado") NOT NULL
);

CREATE TABLE Edicion (
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  lugar VARCHAR(60),
  fecha_inicio DATE,
  fecha_fin DATE,
  horario TIME,
  id_curso INT UNSIGNED,
  id_empleado_capacitado INT UNSIGNED,
  FOREIGN KEY (id_curso) REFERENCES Curso(id),
  FOREIGN KEY (id_empleado_capacitado) REFERENCES Empleado(id)
);

CREATE TABLE empleado_recibe_formacion (
  id_empleado INT UNSIGNED PRIMARY KEY,
  id_edicion INT UNSIGNED, 
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id),
  FOREIGN KEY (id_edicion) REFERENCES Edicion(id)
);

CREATE DATABASE escuela;

USE escuela;

CREATE TABLE alumnos(
    id_alumno int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre varchar(50) NOT NULL,
    lastname varchar(50) NOT NULL,
    lastname2 varchar(50) NOT NULL,
    Matricula int(20) NOT NULL,
    Edad int(3) NOT NULL,
    Fecha date,
    Sexo varchar(20) NOT NULL,
    Estado varchar(20) NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET=latin1;


INSERT INTO alumnos(Nombre, lastname, lastname2, Matricula, Edad, Fecha, Sexo, Estado)
values
('Janeth', 'Atenco', 'Franco', '1718110376', '22', '1998/03/24', 'Femenino', 'Soltera'),
('Fatima', 'Perez', 'Cruz', '1718110402', '20', '2000/02/17', 'Femenino', 'Soltera');

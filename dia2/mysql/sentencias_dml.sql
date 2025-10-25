--sentencias dml
--crud
--c- insert
--r-select
--u-update
--d-delete  

--insert
insert into alumno(nro_documento,name) values('12345678','Josue Guzman');

--insert varios registros
insert into alumno(nro_documento,name,nota)
 values
('87654321','Ana Perez',15),
('11223344','Luis Ramirez',18),
('44332211','Maria Lopez',20),
('55667788','Carlos Sanchez',12),
('99887766','Sofia Torres',17),
('66778899','Diego Flores',14),
('33445566','Elena Rojas',19),
('22113344','Jorge Medina',16),
('77889900','Laura Castillo',13);

--actualizar datos
UPDATE alumno set email= 'codigo@gmail.com';

--actualizar con condicion
UPDATE alumno set email = 'josue@gmail.com' where id = 1;

--actualizar con funciones
UPDATE alumno set email = CONCAT(name,'@gmail.com'); WHERE id != 1;

--eliminar registros
DELETE FROM alumno WHERE id = 10;

-- SELECCIONAR

-- seleccionar todos los campos
SELECT * FROM alumno;

-- seleccionar solo algunos campos
SELECT name,nota from alumno;
-- seleccionar con filtros
SELECT name,nota from alumno where nota > 15;


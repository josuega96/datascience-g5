CREATE TABLE alumno(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    nro_documento VARCHAR(20) NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(100) 
);

--modificar tabla
ALTER TABLE alumno 
    ADD COLUMN nota INT DEFAULT 0 ;

--eliminar tabla
DROP TABLE alumno;
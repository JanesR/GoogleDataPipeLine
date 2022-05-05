create database googleTeste;
use googleTeste;
CREATE TABLE Persons (
    Personid int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (Personid)
);

INSERT INTO Persons (FirstName,LastName)
VALUES ('Lars','Monsen');

INSERT INTO Persons (FirstName,LastName)
VALUES ('Lars','Monsen');

INSERT INTO Persons (FirstName,LastName)
VALUES ('Lars','Monsen');


select Personid,FirstName,LastName from Persons


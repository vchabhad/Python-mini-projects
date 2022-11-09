SHOW DATABASES;
CREATE DATABASE assignment1;

USE assignment1;

CREATE TABLE IF NOT EXISTS SalesPeople (
Snum INT UNSIGNED NOT NULL,
Sname VARCHAR(100) NOT NULL DEFAULT 'name',
City VARCHAR(100) NOT NULL DEFAULT 'city',
Comm INT UNSIGNED NOT NULL DEFAULT 00 ,
PRIMARY KEY (Snum)
);

INSERT INTO SalesPeople VALUES 
(1001,'Peel','London',12),
(1002,'Serres','Sanjose',13),
(1004,'Motika','London',11),
(1007,'Rifkin','Barcelona',15),
(1003,'Axelrod','Newyork',10);

CREATE TABLE IF NOT EXISTS Customers (
 Cnum INT UNSIGNED NOT NULL, 
 Cname  VARCHAR(100) NOT NULL,
 City VARCHAR(100) NOT NULL,
 Snum INT UNSIGNED NOT NULL,
 PRIMARY KEY(Cnum),
 FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum)
 );

INSERT INTO Customers VALUES
(2001, 'Hoffman', 'London', 1001),
(2002, 'Giovanni', 'Rome', 1003),
(2003, 'Liu', 'Sanjose', 1002),
(2004, 'Grass', 'Berlin', 1002),
(2006, 'Clemens', 'London', 1001),
(2008, 'Cisneros', 'Sanjose', 1007),
(2007, 'Pereira', 'Rome', 1004);

CREATE TABLE IF NOT EXISTS Orders (
Onum INT UNSIGNED NOT NULL,
Amt DECIMAL(7,2),
Odate DATE NOT NULL DEFAULT '00-00-0000',
Cnum INT UNSIGNED NOT NULL,
Snum INT UNSIGNED NOT NULL,
PRIMARY KEY (Onum),
FOREIGN KEY (Cnum) REFERENCES Customers(Cnum),
FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum)
);

INSERT INTO Orders VALUES
(3001,18.69,'3-10-1990',2008,1007),
(3003,767.19,'3-10-1990',2001,1001),
(3002,1900.10,'3-10-1990',2007,1004),
(3005,5160.45,'3-10-1990',2003,1002),
(3006,1098.16,'3-10-1990',2008,1007),
(3009,1713.23,'4-10-1990',2002,1003),
(3007,75.75,'4-10-1990',2004,1002),
(3008,4273.00,'5-10-1990',2006,1001),
(3010,1309.95,'6-10-1990',2004,1002),
(3011,9891.88,'6-10-1990',2006,1001);

SELECT * FROM Orders;
SELECT COUNT(Sname) FROM SalesPeople WHERE Sname LIKE 'A%' or 'a%';
SELECT Snum FROM orders GROUP BY Snum HAVING SUM(Amt) > 2000;
SELECT COUNT(Sname) FROM salespeople WHERE City LIKE 'Newyork';
SELECT COUNT(Sname) FROM salespeople WHERE City LIKE 'London' OR City LIKE 'Paris';
SELECT Snum,Odate,count(*) FROM orders GROUP BY Odate,Snum ;
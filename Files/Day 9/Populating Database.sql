-- Inserting Values into the tables.

-- Chennai
INSERT INTO Employee VALUES(100,'Ashwini','Singh','1996-03-27','M',250000,NULL,NULL);
INSERT INTO Branch VALUES(1,'Chennai',100,'2006-02-09');
UPDATE Employee
SET branch_id=1
where emp_id=100;

INSERT INTO Employee VALUES(101,'Abheesta','Vemuru','1997-08-16','M',110000,100,1);

-- Delhi
INSERT INTO Employee VALUES(102,'Abinash','Beuria','1996-09-02','M',75000,100,NULL);
INSERT INTO Branch VALUES(2,'Delhi',102,'1992-04-06');
UPDATE Employee
SET branch_id=2
where emp_id=102;

INSERT INTO Employee VALUES(103,'Aditya','Mohan','1997-08-01','M',63000,102,2);
INSERT INTO Employee VALUES(104,'Anusri','Radha','1997-02-05','F',55000,102,2);
INSERT INTO Employee VALUES(105,'Abhiram','Kumar','1997-03-11','M',69000,102,2);

-- Hyderabad
INSERT INTO Employee VALUES(106,'Ashutosh','Singh','1997-10-11','M',78000,100,NULL);
INSERT INTO Branch VALUES(3,'Hyderabad',106,'1992-04-06');
UPDATE Employee
SET branch_id=3
where emp_id=106;

INSERT INTO Employee VALUES(107,'Aman','Sinha','1996-11-24','M',65000,106,3);
INSERT INTO Employee VALUES(108,'Aprajita','Shreya','1996-03-28','F',71000,106,3);

-- Branch_Supplier

INSERT INTO Branch_Supplier VALUES(2,'Amazon','Paper');
INSERT INTO Branch_Supplier VALUES(2,'Ebay','Electronics');
INSERT INTO Branch_Supplier VALUES(3,'Jabong','Paper');
INSERT INTO Branch_Supplier VALUES(2,'Zomato','Food');
INSERT INTO Branch_Supplier VALUES(3,'Ebay','Electronics');
INSERT INTO Branch_Supplier VALUES(3,'Amazon','Paper');
INSERT INTO Branch_Supplier VALUES(3,'Drunken Monkey','Food');

-- Client

INSERT INTO Client VALUES(400,'Sathyabama',2);
INSERT INTO Client VALUES(401,'Daily Planet',2);
INSERT INTO Client VALUES(402,'Lex Corp',3);
INSERT INTO Client VALUES(403,'Edx',3);
INSERT INTO Client VALUES(404,'Not Found Services',2);
INSERT INTO Client VALUES(405,'Wayne Manor',3);
INSERT INTO Client VALUES(406,'Lex Corp',2);

-- Works_With

INSERT INTO Works_With VALUES(105,400,55000);
INSERT INTO Works_With VALUES(102,401,267000);
INSERT INTO Works_With VALUES(108,402,22500);
INSERT INTO Works_With VALUES(107,403,5000);
INSERT INTO Works_With VALUES(108,403,12000);
INSERT INTO Works_With VALUES(105,404,33000);
INSERT INTO Works_With VALUES(107,405,26000);
INSERT INTO Works_With VALUES(102,406,15000);
INSERT INTO Works_With VALUES(105,406,130000);
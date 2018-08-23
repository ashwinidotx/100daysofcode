SHOW DATABASES;
--CREATE DATABASE shady;
SHOW TABLES;

CREATE TABLE student1(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    branch VARCHAR(20) default 'Undecided'
);

DESCRIBE student;
--desc student;
DROP TABLE student;


-- INSERTING IN A TABLE
INSERT INTO student1(name,branch) VALUES('Ashwini Singh','CSE');
INSERT INTO student1(name,branch) VALUES('Abheesta Vemuru','CSE');
INSERT INTO student1(name,branch) VALUES('Abinash Beuria','IT');
INSERT INTO student1(name, branch) VALUES("Aditya Mohan Singh","IT");
INSERT INTO student1(name, branch) VALUES('Anusri Radha',"ECE");
INSERT INTO student1(name) VALUES('Aman');
INSERT INTO student1(name,branch) VALUES('Aditya MS','IT');

-- UPDATING AND DELETING
UPDATE student1 SET branch='CSE 2' WHERE branch='IT';
UPDATE student1 SET branch='CSE' WHERE student_id=5;
UPDATE student1 SET branch='Info Tech(IT)' where branch='undecided' OR branch="IT";

DELETE FROM student1 WHERE student_id=4;

-- BASIC QUERIES!
SELECT student1.name,student1.branch
FROM student1
ORDER BY student_id DESC;

SELECT * FROM student1 where branch="CSE" order by name limit 4;
SELECT * FROM student1 where branch<>"CSE" order by name;

SELECT * FROM student1;

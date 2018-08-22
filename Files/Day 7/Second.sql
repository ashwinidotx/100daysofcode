SHOW DATABASES;
#CREATE DATABASE shady;
SHOW TABLES;

CREATE TABLE student(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    branch VARCHAR(20)
);

DESCRIBE student;
#desc student;
DROP TABLE student;

ALTER TABLE student ADD gpa DECIMAL(3,2);
ALTER TABLE student DROP COLUMN gpa;

INSERT INTO student(name,branch) VALUES('Ashwini Singh','CSE');
INSERT INTO student(name,branch) VALUES('Abheesta Vemuru','CSE');
INSERT INTO student(name,branch) VALUES('Abinash Beuria','IT');
INSERT INTO student(name, branch) VALUES("Aditya Mohan Singh","IT");
INSERT INTO student(name, branch) VALUES('Anusri Radha',"ECE");


SELECT * FROM student;

DROP TABLE student;
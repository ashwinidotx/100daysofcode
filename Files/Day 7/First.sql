SHOW DATABASES;
#CREATE DATABASE shady;
SHOW TABLES;

CREATE TABLE student(
    student_id INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) UNIQUE
);

DESCRIBE student;
#desc student;
DROP TABLE student;

ALTER TABLE student ADD gpa DECIMAL(3,2);
ALTER TABLE student DROP COLUMN gpa;

INSERT INTO student VALUES(55,'Ashwini Singh','CSE');
INSERT INTO student VALUES(04,'Abheesta Vemuru','CSE');
INSERT INTO student VALUES(06,'Abinash Beuria','IT');
INSERT INTO student VALUES(14,"Aditya Mohan Singh","IT");


INSERT INTO student(name,student_id) VALUES('Aman Sinha',25);
INSERT INTO student VALUES(05,'','ECE');

SELECT * FROM student;

DROP TABLE student;
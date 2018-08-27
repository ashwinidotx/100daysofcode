-- Unions

SELECT first_name,emp_id FROM Employee
UNION
SELECT branch_name,branch_id FROM Branch;
-- ------
SELECT Employee.first_name,Employee.birth_day FROM Employee
UNION
SELECT Branch.branch_name,Branch.branch_id FROM Branch;
-- --
SELECT first_name AS name,emp_id AS ids FROM Employee
UNION
SELECT branch_name,branch_id FROM Branch
UNION
SELECT client_name,client_id FROM Client;

-- Joins
-- 3 types:- JOIN, LEFT JOIN RIHT JOIN
-- Q. find all branches and the name of their managers.
SELECT Employee.emp_id,Employee.first_name,Branch.branch_id
FROM Employee
JOIN Branch
ON emp_id=mgr_id;
-- LJ
SELECT Employee.emp_id,Employee.first_name,Employee.last_name, Branch.branch_name
FROM Employee
LEFT JOIN Branch
ON emp_id=mgr_id;

-- RJ
INSERT INTO Branch VALUES(4,'Patna',NULL,NULL);

SELECT Employee.emp_id,Employee.first_name,Employee.last_name, Branch.branch_name
FROM Employee
RIGHT JOIN Branch
ON emp_id=mgr_id;

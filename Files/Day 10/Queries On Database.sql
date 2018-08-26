
SELECT * FROM Employee;
SELECT * FROM Branch;
SELECT * FROM Client;
SELECT * FROM Works_With;
SELECT * FROM Branch_Supplier;
-- ----------------------------------------------------------------

SELECT * FROM Employee ORDER BY salary;
SELECT * FROM Employee ORDER BY sex DESC, first_name, last_name;
SELECT * FROM Employee LIMIT 5;
-- ------------------------------------------------------------------

SELECT first_name AS forename,last_name AS surname FROM Employee;
-- Find diff genders,branch_id
SELECT DISTINCT sex FROM Employee;
SELECT DISTINCT branch_id FROM Employee;
-- --------------------------------------------------------------------

SELECT * FROM Employee WHERE emp_id>102 ORDER BY salary DESC LIMIT 3;

SELECT first_name,salary from Employee ORDER BY salary DESC;
-- ------------------------------------------------------------

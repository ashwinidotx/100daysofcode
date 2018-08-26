-- SOME FUNCTIONS 

-- COUNT()
SELECT COUNT(emp_id) as NoOfPeople FROM Employee;
SELECT COUNT(super_id) FROM Employee;

-- Display count of male employees born after 1996
SELECT COUNT(emp_id) FROM Employee
WHERE sex='M' AND birth_day >'1996-01-01';

-- AVG(),SUM()
SELECT AVG(salary) FROM Employee WHERE sex='F';
SELECT SUM(salary) AS income FROM Employee;

-- Aggregation!
-- Find out how many males and females there are.
SELECT COUNT(sex), sex
FROM Employee GROUP BY sex;

-- Find Total Sales(Works_With) of Each Salesmen
SELECT SUM(total_sales),emp_id
FROM Works_With GROUP BY emp_id;

-- Expenditure of Each Client
SELECT SUM(total_sales),client_id
FROM Works_With GROUP BY client_id;

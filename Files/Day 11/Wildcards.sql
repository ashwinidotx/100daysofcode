-- WildCards

-- % means any no. of characters, _ means one character
Select * from client;
SELECT * FROM CLIENT 
WHERE client_name LIKE '%corp';

select * from branch_supplier;

UPDATE Branch_Supplier
SET supplier_name='Amazon.com'
where supply_type='Paper' ;

SELECT * FROM branch_supplier WHERE supplier_name like '%com';

-- Find employees born in October

SELECT * FROM Employee 
WHERE birth_day LIKE '%-03-%';
-- Find any Clients who are Colleges
Select * from Client;
UPDATE client
SET client_name = "Sathyabama University"
where client_name = 'Sathyabama';

SELECT * FROM CLIENT
WHERE client_name LIKE '%University';
DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES('added new employee');
    END$$
DELIMITER ;
INSERT INTO employee
VALUES(109, 'Aravind', 'R', '1998-03-19', 'M', 69000, 106, 3);


DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES(NEW.first_name);
    END$$
DELIMITER ;
INSERT INTO employee
VALUES(110, 'Batman', 'Vayne', '1993-4-12', 'M', 69000, 106, 3);

DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
         IF NEW.sex = 'M' THEN
               INSERT INTO trigger_test VALUES('Male Added');
         ELSEIF NEW.sex = 'F' THEN
               INSERT INTO trigger_test VALUES('Femal Added');
         ELSE
               INSERT INTO trigger_test VALUES('Added Emp');
         END IF;
    END$$
DELIMITER ;
INSERT INTO employee
VALUES(111, 'Aakash', 'Kumar', '1998-09-01', 'M', 69000, 106, 3);


DROP TRIGGER my_trigger;
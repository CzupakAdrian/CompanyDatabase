-- Master Tokyo tworzenie dziennika
CREATE TABLE insurers (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);

CREATE SNAPSHOT LOG
ON insurers
WITH PRIMARY KEY;

-- Slave Rio tworzenie snapshota insurers odświerzanie 10s
CREATE SNAPSHOT insurers
BUILD IMMEDIATE
REFRESH FAST
NEXT SYSDATE+(1/(24*60*6))
AS
SELECT id, name FROM insurers@tokyo_link;

-- Obie bazy
CREATE OR REPLACE VIEW insurers_local AS
SELECT * FROM insurers;

-- Sarajevo insert trigger
CREATE OR REPLACE TRIGGER insert_insurers
INSTEAD OF INSERT ON insurers_local
BEGIN
    INSERT INTO insurers_local@tokyo_link (id, name) VALUES(:new.id, :new.name);
END;

-- Tokyo insert trigger
CREATE OR REPLACE TRIGGER insert_insurers
INSTEAD OF INSERT ON insurers_local
FOR EACH ROW
DECLARE
    next_id int;
BEGIN
    SELECT max(id) + 1 INTO next_id FROM insurers;
    INSERT INTO insurers (id, name) VALUES(next_id, :new.name);
END;

-- Sarajevo delete trigger
CREATE OR REPLACE TRIGGER delete_insurers
INSTEAD OF DELETE ON insurers_local
BEGIN
    DELETE FROM insurers@tokyo_link WHERE id = :old.id;
END;

-- Tokyo delete trigger
CREATE OR REPLACE TRIGGER delete_insurers
INSTEAD OF DELETE ON insurers_local
BEGIN
    DELETE FROM insurers WHERE id = :old.id;
END;
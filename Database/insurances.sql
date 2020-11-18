-- serwer 1 (u mnie sarajevo)
CREATE TABLE insurances (
    id INTEGER NOT NULL PRIMARY KEY,
    expiration_date DATE
);
COMMIT;

CREATE VIEW insurances_global AS
SELECT loc.id, rem.insurer_id, loc.expiration_date
FROM insurances loc
INNER JOIN Master.insurances@tokyo_link rem
ON loc.id = rem.id;
COMMIT;

CREATE OR REPLACE TRIGGER insert_insurances
INSTEAD OF INSERT ON insurances_global
BEGIN
    INSERT INTO insurances@tokyo_link VALUES(:new.id, :new.insurer_id);
    INSERT INTO insurances VALUES(:new.id, :new.expiration_date);
END;
COMMIT;

CREATE OR REPLACE TRIGGER delete_insurances
INSTEAD OF DELETE ON insurances_global
BEGIN
    DELETE FROM insurances@tokyo_link rem WHERE :old.id = rem.id;
    DELETE FROM insurances rem WHERE :old.id = rem.id;
END;
COMMIT;

-- serwer 2 (u mnie tokyo)
CREATE TABLE insurances (
    id INTEGER NOT NULL PRIMARY KEY,
    insurer_id INTEGER
);
COMMIT;

CREATE VIEW insurances_global AS
SELECT loc.id, loc.insurer_id, rem.expiration_date
FROM insurances loc
INNER JOIN Master.insurances@sarajevo_link rem
ON loc.id = rem.id;
COMMIT;

CREATE OR REPLACE TRIGGER insert_insurances
INSTEAD OF INSERT ON insurances_global
BEGIN
    INSERT INTO insurances VALUES(:new.id, :new.insurer_id);
    INSERT INTO insurances@sarajevo_link VALUES(:new.id, :new.expiration_date);
END;
COMMIT;

CREATE OR REPLACE TRIGGER delete_insurances
INSTEAD OF DELETE ON insurances_global
BEGIN
    DELETE FROM insurances rem WHERE :old.id = rem.id;
    DELETE FROM insurances@sarajevo_link rem WHERE :old.id = rem.id;
END;
COMMIT;

-- serwer 1 (u mnie sarajevo)
CREATE TABLE insurances (
    id INTEGER NOT NULL,
    expiration_date DATE
);

CREATE VIEW insurances_global AS
SELECT loc.id, rem.insurer_id, loc.expiration_date
FROM insurances loc
INNER JOIN Master.insurances@tokyo_link rem
ON loc.id = rem.id;


-- serwer 2 (u mnie tokyo)
CREATE TABLE insurances (
    id INTEGER NOT NULL,
    insurer_id INTEGER
);

CREATE VIEW insurances_global AS
SELECT loc.id, loc.insurer_id, rem.expiration_date
FROM insurances loc
INNER JOIN Master.insurances@sarajevo_link rem
ON loc.id = rem.id;
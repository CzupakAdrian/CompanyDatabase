CREATE TABLE positions (
    id INTEGER NOT NULL,
    position VARCHAR(20) NOT NULL,
    CONSTRAINT both_unique UNIQUE (id, position)
);

-- just for triggering
CREATE VIEW positions_global
AS SELECT position FROM positions;

CREATE OR REPLACE TRIGGER insert_position
INSTEAD OF INSERT ON positions_global
FOR EACH ROW
DECLARE
    next_id INTEGER;
BEGIN
    SELECT max(id)+1 INTO next_id FROM positions;
    INSERT INTO positions VALUES (next_id, :new.position);
    INSERT INTO positions@sarajevo_link VALUES (next_id, :new.position);
    -- dopisać dla wszystkich linków
END;


-- fragmentacja pozioma workers - INSERT
-- globalna insercja workersów
CREATE OR REPLACE NONEDITIONABLE TRIGGER insert_global_workers
INSTEAD OF INSERT ON workers_global
FOR EACH ROW
DECLARE 
    location VARCHAR2(10);
    next_id int;
BEGIN
    SELECT name INTO location FROM locations_global WHERE id=:new.location_id;
    SELECT max(id) + 1 INTO next_id FROM workers_global;
    IF location = 'Tokyo' THEN -- zmienić warunki
        INSERT INTO workers_global@tokyo_link (id, name, surname, birth_date, position_id, location_id, insurance_id) -- zmienić link i dodać inne
        VALUES (next_id, :new.name, :new.surname, :new.birth_date, :new.position_id, :new.location_id, :new.insurance_id);
    ELSE
        SELECT max(id)+1 INTO next_id FROM workers;
        INSERT INTO workers (id, name, surname, birth_date, position_id, location_id, insurance_id)
        VALUES (next_id, :new.name, :new.surname, :new.birth_date, :new.position_id, :new.location_id, :new.insurance_id);
    END IF;
END;

-- DELETE
CREATE OR REPLACE NONEDITIONABLE TRIGGER delete_workers
INSTEAD OF DELETE ON workers_global
FOR EACH ROW
DECLARE 
    location VARCHAR2(10);
    loc_id int;
    BEGIN
        SELECT location_id INTO loc_id FROM workers_global WHERE id = :old.id;
        SELECT name INTO location FROM locations WHERE id=loc_id;
        IF location = 'Tokyo' THEN -- zmienić warunki
            DELETE FROM workers@tokyo_link WHERE id = :old.id; -- zmienić link i dodać inne
        ELSE
            DELETE FROM workers WHERE id = :old.id;
        END IF;
    END;

-- UPDATE
CREATE OR REPLACE NONEDITIONABLE TRIGGER update_workers
INSTEAD OF UPDATE ON workers_global
FOR EACH ROW
DECLARE 
    location VARCHAR2(10);
    loc_id int;
    BEGIN
        SELECT location_id INTO loc_id FROM workers_global WHERE id = :old.id;
        SELECT name INTO location FROM locations WHERE id=loc_id;
        IF location = 'Tokyo' THEN -- zmienić warunki
            UPDATE workers@tokyo_link SET name=:new.name, surname=:new.surname, birth_date=:new.birth_date, -- zmienić link i dodać inne
                                        position_id=:new.position_id, location_id=:new.location_id, insurance_id=:new.insurance_id
            WHERE id = :new.id;
        ELSE
            UPDATE workers SET name=:new.name, surname=:new.surname, birth_date=:new.birth_date, 
                                        position_id=:new.position_id, location_id=:new.location_id, insurance_id=:new.insurance_id
            WHERE id = :new.id;
        END IF;
    END;
-- widok do wyświetlania workersów i wstawiania w odpowiednie miejsce
CREATE view all_workers AS
SELECT * FROM workers
UNION
SELECT * FROM workers@tokyo_link;

-- fragmentacja pozioma workers - INSERT
CREATE OR replace NONEDITIONABLE trigger INSERT_workers
INSTEAD OF INSERT ON all_workers
FOR EACH ROW
DECLARE 
    location VARCHAR2(10);
    next_id int;
    BEGIN
        SELECT name INTO location FROM locations WHERE id=:new.location_id;
        SELECT max(id) + 1 INTO next_id FROM all_workers;
        IF location = 'tokyo' THEN
            INSERT INTO workers@tokyo_link VALUES(next_id, :new.name, :new.surname, :new.birth_date, :new.position_id, :new.location_id,
                                            :new.insurance_id);
        ELSE
            INSERT INTO workers VALUES(next_id, :new.name, :new.surname, :new.birth_date, :new.position_id, :new.location_id,
                                            :new.insurance_id);
        END IF;
  END;

-- DELETE
CREATE OR replace NONEDITIONABLE trigger DELETE_workers
INSTEAD OF DELETE ON all_workers
FOR EACH ROW
DECLARE 
    location VARCHAR2(10);
    loc_id int;
    BEGIN
        SELECT location_id INTO loc_id FROM all_workers WHERE id = :old.id;
        SELECT name INTO location FROM locations WHERE id=loc_id;
        IF location = 'tokyo' THEN
            DELETE FROM workers@tokyo_link WHERE id = :old.id;
        ELSE
            DELETE FROM workers WHERE id = :old.id;
        END IF;
    END;

-- UPDATE
CREATE OR replace NONEDITIONABLE trigger update_workers
INSTEAD OF UPDATE on all_workers
FOR EACH ROW
DECLARE 
    location VARCHAR2(10);
    loc_id int;
    BEGIN
        SELECT location_id INTO loc_id FROM all_workers WHERE id = :old.id;
        SELECT name INTO location FROM locations WHERE id=loc_id;
        IF location = 'tokyo' THEN
            UPDATE workers@tokyo_link SET name=:new.name, surname=:new.surname, birth_date=:new.birth_date, 
                                        position_id=:new.position_id, location_id=:new.location_id, insurance_id=:new.insurance_id
            WHERE id = :new.id;
        ELSE
            UPDATE workers SET name=:new.name, surname=:new.surname, birth_date=:new.birth_date, 
                                        position_id=:new.position_id, location_id=:new.location_id, insurance_id=:new.insurance_id
            WHERE id = :new.id;
        END IF;
    END;
-- widok do wyświetlania wszystkich preferences i wstawiania w odpowiednie miejsce
CREATE view workers_preferences_global AS
SELECT * FROM workers_preferences
UNION
SELECT * FROM workers_preferences@tokyo_link;

-- fragmentacja pozioma workers preferences - INSERT
CREATE OR replace NONEDITIONABLE trigger INSERT_workers_preferences
INSTEAD OF INSERT ON workers_preferences_global
FOR EACH ROW
DECLARE 
    location VARCHAR2(10);
    loc_id int;
    BEGIN
        SELECT location_id INTO loc_id FROM workers WHERE id=:new.worker_id;
        SELECT name INTO location FROM locations WHERE id=loc_id;
        IF location = 'tokyo' THEN
            INSERT INTO workers_preferences@tokyo_link VALUES(:new.worker_id, :new.location_id);
        ELSE
            INSERT INTO workers_preferences VALUES(:new.worker_id, :new.location_id);
        END IF;
    END;

-- DELETE
CREATE OR replace NONEDITIONABLE trigger DELETE_workers_preferences
INSTEAD OF DELETE ON workers_preferences_global
FOR EACH ROW
DECLARE 
    location VARCHAR2(10);
    loc_id int;
    BEGIN
        SELECT location_id INTO loc_id FROM workers_global WHERE id = :old.worker_id;
        SELECT name INTO location FROM locations WHERE id=loc_id;
        IF location = 'tokyo' THEN
            DELETE FROM workers_preferences@tokyo_link WHERE worker_id = :old.worker_id;
        ELSE
            DELETE FROM workers_preferences WHERE worker_id = :old.worker_id;
        END IF;
    END;

-- UPDATE
CREATE OR replace NONEDITIONABLE trigger update_workers_preferences
INSTEAD OF UPDATE on workers_preferences_global
FOR EACH ROW
DECLARE 
    location VARCHAR2(10);
    loc_id int;
    BEGIN
        SELECT location_id INTO loc_id FROM workers_global WHERE id = :old.worker_id;
        SELECT name INTO location FROM locations WHERE id=loc_id;
        IF location = 'tokyo' THEN
            UPDATE workers_preferences@tokyo_link SET worker_id=:new.worker_id, location_id=:new.location_id
            WHERE worker_id = :new.worker_id;
        ELSE
            UPDATE workers_preferences SET worker_id=:new.worker_id, location_id=:new.location_id
            WHERE worker_id = :new.worker_id;
        END IF;
    END;
-- widok do wyświetlania workersów i wstawiania w odpowiednie miejsce
create view all_workers as
select * from workers
union
select * from workers@tokyo_link;

-- fragmentacja pozioma workers - insert
create or replace NONEDITIONABLE trigger insert_workers
INSTEAD OF insert ON all_workers
for each row
declare 
    location varchar2(10);
    next_id int;
    BEGIN
        select name into location from locations where id=:new.location_id;
        select max(id) + 1 into next_id from all_workers;
        if location = 'tokyo' then
            insert into workers@tokyo_link values(next_id, :new.name, :new.surname, :new.birth_date, :new.position_id, :new.location_id,
                                            :new.insurance_id);
        else
            insert into workers values(next_id, :new.name, :new.surname, :new.birth_date, :new.position_id, :new.location_id,
                                            :new.insurance_id);
        end if;
  END;

-- delete
create or replace NONEDITIONABLE trigger delete_workers
instead of delete ON all_workers
for each row
declare 
    location varchar2(10);
    loc_id int;
    BEGIN
        select location_id into loc_id from all_workers where id = :old.id;
        select name into location from locations where id=loc_id;
        if location = 'tokyo' then
            delete from workers@tokyo_link where id = :old.id;
        else
            delete from workers where id = :old.id;
        end if;
    END;

-- update
create or replace NONEDITIONABLE trigger update_workers
instead of update on all_workers
for each row
declare 
    location varchar2(10);
    loc_id int;
    begin
        select location_id into loc_id from all_workers where id = :old.id;
        select name into location from locations where id=loc_id;
        if location = 'tokyo' then
            update workers@tokyo_link set name=:new.name, surname=:new.surname, birth_date=:new.birth_date, 
                                        position_id=:new.position_id, location_id=:new.location_id, insurance_id=:new.insurance_id
            where id = :new.id;
        else
            update workers set name=:new.name, surname=:new.surname, birth_date=:new.birth_date, 
                                        position_id=:new.position_id, location_id=:new.location_id, insurance_id=:new.insurance_id
            where id = :new.id;
        end if;
    end;
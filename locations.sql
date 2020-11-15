-- Master Tokyo locations ograniczenie read only 
ALTER TABLE locations READ ONLY;

-- Slave Rio tworzenie snapshota locations brak odświerzania
CREATE SNAPSHOT locations
BUILD IMMEDIATE
REFRESH COMPLETE
AS 
SELECT id, name FROM locations@tokyo_link;
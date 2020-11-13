-- Slave Rio tworzenie snapshota locations brak odświerzania
CREATE SNAPSHOT locations_remote
BUILD IMMEDIATE
REFRESH COMPLETE
AS 
SELECT id, name FROM locations@tokyo_link; -- dopisać linki

CREATE VIEW locations_global
AS SELECT * FROM locations
UNION SELECT * FROM locations_remote;
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
CREATE TABLE insurers (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);

-- Master Tokyo tworzenie dziennika
CREATE SNAPSHOT LOG
ON insurers
WITH PRIMARY KEY;
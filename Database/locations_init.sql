-- Master Tokyo locations ograniczenie read only 
CREATE TABLE locations (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);
INSERT INTO locations VALUES(1, 'Sarajevo');
INSERT INTO locations VALUES(2, 'Tokyo');
ALTER TABLE locations READ ONLY;
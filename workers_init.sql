CREATE TABLE workers (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    birth_date DATE NOT NULL,
    position_id INT NOT NULL,
    location_id INT,
    insurance_id INT
);

-- widok do wyświetlania workersów i wstawiania w odpowiednie miejsce
CREATE OR REPLACE VIEW workers_global AS
    SELECT * FROM workers
    UNION
    SELECT * FROM workers@tokyo_link; -- dodać linki

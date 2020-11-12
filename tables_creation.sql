CREATE TABLE workers (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    birth_date DATE NOT NULL,
    position_id INT NOT NULL,
    location_id INT,
    insurance_id INT
);

CREATE TABLE positions (
    id INT NOT NULL PRIMARY KEY,
    position VARCHAR(20) NOT NULL
);

CREATE TABLE insurances (
    id INT NOT NULL PRIMARY KEY,
    insurer_id INT NOT NULL,
    expiration_date DATE
);

CREATE TABLE insurers (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);

CREATE TABLE locations (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);

CREATE TABLE workers_preferences (
    worker_id INT NOT NULL,
    location_id INT NOT NULL
);
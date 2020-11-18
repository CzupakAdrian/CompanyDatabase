-- Klucz obcy locations id w workers obie bazy danych
ALTER TABLE workers
ADD CONSTRAINT fk_location FOREIGN KEY (location_id)
REFERENCES locations(id);

ALTER TABLE workers
ADD CONSTRAINT fk_position FOREIGN KEY (position_id)
REFERENCES positions(id);

ALTER TABLE workers
ADD CONSTRAINT fk_inurance FOREIGN KEY (insurance_id)
REFERENCES insurances(id);

-- Klucz obcy locations id w workers preferences obie bazy danych
ALTER TABLE workers_preferences
ADD CONSTRAINT fk_workers_pref_location FOREIGN KEY (location_id)
REFERENCES locations(id);

-- Klucz obcy workers id w workers preferences obie bazy danych - nie może być replikacji na preferences tylko fragmentacja
ALTER TABLE workers_preferences
ADD CONSTRAINT fk_workers_pref_id FOREIGN KEY (worker_id)
REFERENCES workers(id);
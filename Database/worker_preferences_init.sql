CREATE TABLE workers_preferences (
    worker_id INT NOT NULL,
    location_id INT NOT NULL
);

ALTER TABLE workers_preferences
ADD CONSTRAINT fk_worker_id_worker_preferences
   FOREIGN KEY (worker_id)
   REFERENCES workers(id);

ALTER TABLE workers_preferences
ADD CONSTRAINT fk_location_id_worker_preferences
   FOREIGN KEY (location_id)
   REFERENCES locations(id);
CREATE TABLE tests (
    test_id serial PRIMARY KEY,
    bin_size INTEGER, 
    num_of_runs INTEGER,
    runtime INTERVAL
);

INSERT INTO tests(test_id, bin_size, num_of_runs) VALUES(1, 2000, 3);
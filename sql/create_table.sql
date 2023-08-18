DROP TABLE IF EXISTS json_data;

CREATE TABLE IF NOT EXISTS json_data (
    id serial PRIMARY KEY,
    data jsonb
);
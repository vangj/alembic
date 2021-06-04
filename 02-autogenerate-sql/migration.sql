CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 4e9a2a1fe81d

CREATE TABLE person (
    id INTEGER NOT NULL, 
    email VARCHAR, 
    password VARCHAR, 
    first_name VARCHAR, 
    last_name VARCHAR, 
    PRIMARY KEY (id)
);

CREATE INDEX ix_person_email ON person (email);

CREATE INDEX ix_person_first_name ON person (first_name);

CREATE INDEX ix_person_id ON person (id);

CREATE INDEX ix_person_last_name ON person (last_name);

CREATE INDEX ix_person_password ON person (password);

INSERT INTO alembic_version (version_num) VALUES ('4e9a2a1fe81d');


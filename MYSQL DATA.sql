CREATE TABLE petrol (
    volume FLOAT,
    cost INT
);

CREATE TABLE diesel (
    volume FLOAT,
    cost INT
);

CREATE TABLE speed (
    volume FLOAT,
    cost INT
);

CREATE TABLE pet (
    year INT,
    rate FLOAT
);

CREATE TABLE dies (
    year INT,
    rate FLOAT
);

CREATE TABLE speed_p (
    year INT,
    rate FLOAT
);

CREATE TABLE petrol_prices (
    date DATE,
    price FLOAT,
    type VARCHAR(20)
);

CREATE TABLE yearly (
    year INT,
    petrol_rate FLOAT,
    diesel_rate FLOAT,
    speed_rate FLOAT
);

CREATE TABLE entries (
    entry_date DATE,
    entry_time TIME
);

CREATE TABLE house_prices ( id int primary key,
    property_type varchar(32),
    price numeric,
    location varchar(64),
    city varchar(64),
    baths int,
    purpose varchar(256),
    bedrooms int,
    Area_in_Marla numeric
);

COPY house_prices FROM '/house_prices.csv' DELIMITER ',' CSV HEADER;

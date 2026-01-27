CREATE DATABASE sustainability;
USE sustainability;

CREATE TABLE fact_sustainability (
    id INT,
    Product VARCHAR(255),
    Facility VARCHAR(255),
    Year INT,
    Season VARCHAR(50),
    Energy_Use_kWh FLOAT,
    Water_Use_L FLOAT,
    CO2_Emissions_kg FLOAT,
    Waste_kg FLOAT,
    Units_Produced INT,
    CO2_per_unit FLOAT,
    Energy_per_unit FLOAT,
    Water_per_unit FLOAT,
    Waste_per_unit FLOAT
);

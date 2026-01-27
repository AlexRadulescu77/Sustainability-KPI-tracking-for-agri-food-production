
-- Total emissions by year
SELECT 
    Year,
    SUM(CO2_Emissions_kg) as Total_CO2,
    SUM(Energy_Use_kWh) as Total_Energy,
    SUM(Water_Use_L) as Total_Water,
    SUM(Waste_kg) as Total_Waste
FROM fact_sustainability
GROUP BY Year
ORDER BY Year;

-- Calculate average efficiency per product
SELECT 
    Product,
    ROUND(AVG(CO2_per_unit), 3) as Avg_CO2_per_unit,
    ROUND(AVG(Energy_per_unit), 3) as Avg_Energy_per_unit,
    ROUND(AVG(Water_per_unit), 3) as Avg_Water_per_unit,
    ROUND(AVG(Waste_per_unit), 3) as Avg_Waste_per_unit
FROM fact_sustainability
GROUP BY Product
ORDER BY Avg_CO2_per_unit;


-- Best performing facilities by CO2 efficiency
SELECT 
    Facility,
    Product,
    Year,
    ROUND(AVG(CO2_per_unit), 3) as Avg_CO2_Efficiency
FROM fact_sustainability
GROUP BY Facility, Product, Year
ORDER BY Avg_CO2_Efficiency
LIMIT 10;

-- Seasonal trends
SELECT 
    Season,
    Year,
    ROUND(AVG(CO2_per_unit), 3) as Avg_CO2,
    ROUND(AVG(Energy_per_unit), 3) as Avg_Energy
FROM fact_sustainability
GROUP BY Season, Year
ORDER BY Year, Season;

-- Which products produce the least CO2 
SELECT 
    Product,
    ROUND(AVG(CO2_per_unit), 2) as Average_CO2_per_Unit
FROM fact_sustainability
GROUP BY Product
ORDER BY Average_CO2_per_Unit;

-- Best performing batches
SELECT 
    Product,
    Facility,
    Year,
    Season,
    ROUND(CO2_per_unit, 2) as CO2_per_Unit,
    Units_Produced
FROM fact_sustainability
ORDER BY CO2_per_unit
LIMIT 10;

-- And worst performing batches
SELECT 
    Product,
    Facility,
    Year,
    Season,
    ROUND(CO2_per_unit, 2) as CO2_per_Unit,
    Units_Produced
FROM fact_sustainability
ORDER BY CO2_per_unit DESC
LIMIT 10;
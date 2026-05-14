USE world;

-- 1. Countries that speak Slovene
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.code = languages.country_code
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

-- 2. Total number of cities per country
SELECT countries.name, COUNT(cities.id) AS total_cities
FROM countries
JOIN cities ON countries.code = cities.country_code
GROUP BY countries.name
ORDER BY total_cities DESC;

-- 3. Cities in Mexico with population > 500,000
SELECT cities.name, cities.population
FROM cities
JOIN countries ON cities.country_code = countries.code
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;

-- 4. Languages with percentage > 89%
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.code = languages.country_code
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

-- 5. Countries with surface area < 501 and population > 100,000
SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 AND population > 100000;

-- 6. Constitutional Monarchy with capital > 200 and life expectancy > 75
SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy'
AND capital > 200
AND life_expectancy > 75;

-- 7. Cities in Argentina in Buenos Aires district with population > 500,000
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON countries.code = cities.country_code
WHERE countries.name = 'Argentina'
AND cities.district = 'Buenos Aires'
AND cities.population > 500000;

-- 8. Number of countries per region
SELECT region, COUNT(*) AS total_countries
FROM countries
GROUP BY region
ORDER BY total_countries DESC;


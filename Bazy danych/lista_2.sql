Dominik Komla, grupa mpy

-- Zadanie 1

CREATE VIEW SeaAirports (iatacode, name, city, province, country, sea)
AS SELECT airport.iatacode, airport.name, airport.city, airport.province, airport.country, located.sea
FROM Airport JOIN city ON(airport.city = city.name and airport.country = city.country)
JOIN located ON(located.city = airport.city and airport.country = located.country)
WHERE city.elevation > 200 AND sea IS NOT NULL;

-- Zadanie 2

-- usuwanie klucza glownego z tabeli city
ALTER TABLE city DROP constraint citykey;
-- dodanie klumny id jako klucz glowny
ALTER TABLE city ADD column id SERIAL PRIMARY KEY;
-- dodanie kolumny CItyId z typem takim jak id w city
ALTER TABLE airport ADD column CityId Integer;

-- ustawianie wartosci CityId aby odpowiadaly wartosciom w city
UPDATE airport SET CityId = city.id
FROM city
WHERE airport.city = city.name; 

-- dodanie klucza obcego
ALTER TABLE airport ADD FOREIGN KEY(CityId) references City(id);

-- Zadanie 3

INSERT INTO CountryPops (country, year, population)
SELECT country.code, 2021, country.population
FROM country;

-- Zadanie 4

ALTER TABLE country add column poppeakcount numeric;S

UPDATE country SET poppeakcount = g1.population
FROM (SELECT countrypops.country, min(countrypops.year) AS year, countrypops.population FROM countrypops
JOIN (SELECT country, max(population) AS population
FROM countrypops
GROUP BY country) g ON(g.country=countrypops.country AND g.population=countrypops.population)
GROUP BY countrypops.country, countrypops.population) g1
WHERE g1.country = country.code;

ALTER TABLE country add column popPeakYear numeric;

UPDATE country SET poppeakyear = g1.year
FROM (SELECT countrypops.country, min(countrypops.year) AS year, countrypops.population FROM countrypops
JOIN (SELECT country, max(population) AS population
FROM countrypops
GROUP BY country) g ON(g.country=countrypops.country AND g.population=countrypops.population)
GROUP BY countrypops.country, countrypops.population) g1
WHERE g1.country = country.code;



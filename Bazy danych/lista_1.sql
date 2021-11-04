-- Dominik Komła, mpy
-- Zadanie 1

SELECT country.name, COUNT (DISTINCT islandin.island)
FROM country LEFT JOIN geo_sea ON (country.code = geo_sea.country)
LEFT JOIN islandin USING (sea)
GROUP BY country.name
ORDER BY 2 DESC, 1 ASC;

-- Zadanie 2


SELECT p.name, ethnicgroup.percentage
FROM ethnicgroup
JOIN
(SELECT country.name, ethnicgroup.country
FROM country JOIN ethnicgroup ON(country.code = ethnicgroup.country)
GROUP BY country.name, ethnicgroup.country
HAVING COUNT(DISTINCT ethnicgroup.name) >= 10
AND country.name IN(SELECT country.name FROM country JOIN ethnicgroup ON
(country.code = ethnicgroup.country) WHERE ethnicgroup.name = 'Polish'))
p
ON (ethnicgroup.country = p.country)
WHERE ethnicgroup.name = 'Polish';


-- Zadanie 4

SELECT country.name, ((p.sum / country.population) * 100) as city_population_percentage
FROM country JOIN (SELECT country.name, SUM(city.population)
FROM country JOIN city ON(country.code = city.country)
GROUP BY country.name) p ON(p.name = country.name)
WHERE ((p.sum / country.population) * 100) >= 75
ORDER BY 2 DESC;

-- Dominik Komla, grupa mpy

-- Zadanie 0

create table sunken_city (like city);
alter table sunken_city add column sinking_date date;
-- tutaj tworze jeszcze tabele zmienne, gdzie bede trzymal ostatni poziom morza
create table zmienne (name varchar(50), value int);
INSERT INTO zmienne VALUES ('last_sea_level', NULL);

-- Zadanie 1

CREATE OR REPLACE FUNCTION sea_level (level int)
RETURNS void
AS $X$

INSERT INTO sunken_city 
SELECT city.*, NOW() FROM city WHERE city.elevation < level;

DELETE FROM city WHERE city.elevation < level;

DELETE FROM airport WHERE airport.elevation < level;

UPDATE airport
SET city = NULL
WHERE airport.city IN (SELECT name FROM sunken_city);

UPDATE zmienne SET value = level WHERE name = 'last_sea_level';
 	
$X$ LANGUAGE SQL;

-- testowalem to zadanie patrzac jakie miasta sa na danym poziomie morza,
-- i wywowylawem funkcje z ta wartoscia. wtedy patrzylem, czy te miasta
-- zostaly usuniete z city i dodane do sunken_city oraz czy zmienila
-- sie wartosc naszego last_sea_level.




-- Dominik Komla, grupa mpy

-- Zadanie 1

SELECT DISTINCT organization.name 
FROM organization JOIN isMember ON (organization.abbreviation = isMember.organization)
JOIN borders ON (isMember.country = borders.country1) 
JOIN politics poli1 ON (poli1.country = borders.country1)
JOIN politics poli2 ON (poli2.country = borders.country2)
WHERE poli1.independence IS NOT NULL AND
poli2.independence IS NOT NULL AND 
ABS(DATE_PART('year', poli1.independence) 
- DATE_PART('year', poli2.independence)) > 580
AND poli2.country IN (SELECT country FROM isMember 
c1 WHERE c1.organization = isMember.organization);

-- Zadanie 2

CREATE TABLE city_log (
id SERIAL PRIMARY KEY, 
rodzaj varchar(6),
uzytkownik varchar(120),
data timestamp, 
akcept boolean DEFAULT true
);

-- Zadanie 3

CREATE OR REPLACE FUNCTION funkcja_dla_insert() RETURNS TRIGGER AS
$X$
BEGIN
	INSERT INTO city_log(rodzaj, uzytkownik, data)
		VALUES('INSERT', current_user, now());
RETURN NEW;
END
$X$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION funkcja_dla_update() RETURNS TRIGGER AS
$X$
BEGIN
	INSERT INTO city_log(rodzaj, uzytkownik, data)
		VALUES('UPDATE', current_user, now());
RETURN NEW;
END
$X$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION funkcja_dla_delete() RETURNS TRIGGER AS
$X$
BEGIN
	INSERT INTO city_log(rodzaj, uzytkownik, data)
		VALUES('DELETE', current_user, now());
RETURN NEW;
END
$X$ LANGUAGE plpgsql;


CREATE TRIGGER on_insert_to_city AFTER INSERT ON city
FOR EACH ROW EXECUTE PROCEDURE funkcja_dla_insert();

CREATE TRIGGER on_update_to_city AFTER UPDATE ON city
FOR EACH ROW EXECUTE PROCEDURE funkcja_dla_update();

CREATE TRIGGER on_delete_to_city AFTER DELETE ON city
FOR EACH ROW EXECUTE PROCEDURE funkcja_dla_delete();


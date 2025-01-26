
-- 1. Вывести названия стран и названия сопоставленных им столиц


  SELECT country.name, city.name
  FROM        country 
  INNER JOIN     city 
  ON           country.Capital = city.id;
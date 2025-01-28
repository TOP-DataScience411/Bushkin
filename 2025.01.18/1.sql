
-- 1. Вывести названия стран и названия сопоставленных им столиц


  SELECT    country.name, 
            city.name
  FROM        country 
  INNER JOIN     city 
  ON           country.Capital = city.id;

-- 2. Сравнить по регионам сумму населения стран и сумму населения городов


  SELECT sum(DISTINCT country.Population),
         sum(city.Population),
         Region
  FROM          country 
  INNER JOIN    city
  ON            Code = CountryCode
  GROUP BY      Region;

-- 3. Вывести десять языков, на которых разговаривает больше всего людей

  SELECT  language,
          sum( Percentage / 100 * c.Population) AS total
  FROM        countrylanguage AS cl
  INNER JOIN  country AS c
  ON          CountryCode = Code
  GROUP BY    language
  ORDER BY    total   DESC
  LIMIT 10;
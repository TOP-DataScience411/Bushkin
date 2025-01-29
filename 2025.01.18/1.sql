
-- 1. Вывести названия стран и названия сопоставленных им столиц


      SELECT    country.name, 
                city.name
        FROM    country 
  INNER JOIN    city 
          ON    country.Capital = city.id;

-- 2. Сравнить по регионам сумму населения стран и сумму населения городов


      SELECT    sum(DISTINCT country.Population),
                sum(city.Population),
                Region
        FROM    country 
  INNER JOIN    city
          ON    Code = CountryCode
    GROUP BY    Region;

-- 3. Вывести десять языков, на которых разговаривает больше всего людей

      SELECT   language,
               sum( Percentage / 100 * c.Population) AS total
        FROM   countrylanguage AS cl
  INNER JOIN   country AS c
          ON   CountryCode = Code
    GROUP BY   language
    ORDER BY   total   DESC
       LIMIT   10;


--4. Вывести названия специальностей и суммарное количество дней отпусков, в которых были врачи каждой специальности; отсортировать по возрастанию суммарного количества дней отпуска

      SELECT   s.name, 
               sum(end_date - start_date) AS sum_al
        FROM   vacations as v
        JOIN   doctors_specs AS d_s
          ON   v.doctor_id = d_s.doctor_id
        JOIN   specializations AS s
          ON   spec_id = s.id
    GROUP BY   s.name
    ORDER BY   sum_al; 



--5. Вывести округлённую до целого сумму средств, которую можно выделить на одну палату этого отделения (в зависимости от количества палат в отделении), от всех пожертвований каждому отделению; отсортировать по убыванию найденной суммы


      SELECT  d.name, round(sum(DISTINCT amount)/count(DISTINCT w.name)) AS per_ward
        FROM  departments as d
        JOIN  donations as don
          ON  d.id=don.dep_id
        JOIN  wards as w
          ON  d.id = w.dep_id
    GROUP BY  d.name
    ORDER BY  per_ward DESC;
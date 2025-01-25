-- 1. Вывести средний оклад (salary) всех сотрудников

 SELECT round(avg(salary),2) AS avg_salary
 FROM doctors;

 -- avg_salary
-- ----------
 -- 56401.29

-- 2. Вывести среднюю премию для всех сотрудников, чей доход выше среднего (взять явное значение из результата предыдущего запроса)


 SELECT round(avg(premium),2) AS avg_premium
 FROM doctors
 WHERE SALARY > 56401.29;

--3. Вывести с сортировкой по возрастанию среднее количество дней в отпуске для каждого сотрудника — в MySQL используйте функцию datediff(), в PostgreSQL используйте вычитание с помощью оператора -

 SELECT round(avg(end_date-start_date),0) AS days
 FROM vacations
 GROUP BY doctor_id
 ORDER BY days;

--4. Вывести для каждого сотрудника самый ранний год отпуска и самый поздний год отпуска с сортировкой по возрастанию разности между этими двумя значениями

 SELECT doctor_id,
        min(extract(year FROM start_date)) AS min_year,
        max(extract(year FROM end_date)) AS max_year
 FROM vacations
 GROUP BY doctor_id
 ORDER BY max(extract(year FROM end_date)) - max(extract(year FROM end_date));

--5. Вывести сумму пожертвований за всё время для каждого отделения с сортировкой по возрастанию номеров отделений


 SELECT dep_id, sum(amount)
 FROM donations
 GROUP BY dep_id
 ORDER BY dep_id;


--6. Вывести сумму пожертвований за каждый год для каждого спонсора с сортировкой по возрастанию номеров спонсоров и годов

 SELECT sponsor_id, 
        extract(year from date), 
        sum(amount)
 FROM 
        donations
 GROUP BY sponsor_id,
          extract(year from date)
 ORDER BY sponsor_id,
          extract(year from date);

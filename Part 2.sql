

#Question1
SELECT date_trunc('month', users.created_at) AS cohort_month,
(SELECT COUNT(*) FROM users GROUP BY date_trunc('month', users.created_at) INNER JOIN exercises ON users.user_id = exercises.user_id
 WHERE DATEDIFF(month, date_trunc('month', exercises.exercise_completion_date), date_trunc('month', users.created_at))=1)* 100 / (SELECT COUNT(*) FROM users GROUP BY date_trunc('month', users.created_at)) AS percentage
FROM users;


#Question2
SELECT COUNT(CASE WHEN (SELECT COUNT(user_id) FROM exercises GROUP by user_id) > 0 THEN 1 END) AS NumberOfOneactivity,
COUNT(CASE WHEN (SELECT COUNT(user_id) FROM exercises GROUP by user_id) > 9 THEN 1 END) AS NumberOfTenactivities,
COUNT(CASE WHEN (SELECT COUNT(user_id) FROM exercises GROUP by user_id) > 99 THEN 1 END) AS NumberOfHunredactivities,
COUNT(CASE WHEN (SELECT COUNT(user_id) FROM exercises GROUP by user_id) > 999 THEN 1 END) AS NumberOfThousandactivities,
FROM exercises;




#Question3
SELECT Providers.organization_name, AVG(Phq9.score))
  FROM Providers
     INNER JOIN Phq9
        ON Providers.provider_id = Phq9.provider_id
  GROUP BY Providers.organization_name
  ORDER BY AVG(Phq9.score) DESC
  LIMIT 5;

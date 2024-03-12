-- displays the top 3 of cities temperature during July and August
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP by city
ORDER by avg_temp DESC
LIMIT 3;

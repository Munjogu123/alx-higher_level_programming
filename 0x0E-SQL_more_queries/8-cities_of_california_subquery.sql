-- lists all the cities of California that can be found in the database
SELECT cities.id, cities.name
FROM states, cities
WHERE cities.state_id = 1
AND states.id = cities.state_id
ORDER BY cities.id

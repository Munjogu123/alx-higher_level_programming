-- displays the max temperature of each state
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP by state
ORDER by state;

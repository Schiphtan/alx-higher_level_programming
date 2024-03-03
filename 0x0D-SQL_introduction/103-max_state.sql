-- Displays the max temperature of each state, Order by name.
SELECT state, MAX(value) as max_tempe
FROM temperatures
GROUP BY state
ORDER BY state;

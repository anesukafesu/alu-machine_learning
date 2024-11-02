-- Groups entries by city
-- Averages the entries
-- Displays them in descending order
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
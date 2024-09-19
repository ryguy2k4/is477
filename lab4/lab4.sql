SELECT airlines.name AS carrier_name, AVG(dep_delay) as dep_delay
FROM flights, airlines
WHERE flights.carrier = airlines.carrier
GROUP BY carrier_name
ORDER BY dep_delay ASC
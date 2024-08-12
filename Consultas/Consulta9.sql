Use Seminario2
SELECT TOP 5
    p.Gender,
    p.Age,
    COUNT(v.HechoID) AS FlightCount
FROM 
    Vuelo v
JOIN 
    Pasajero p ON v.PassengerID = p.PassengerID
GROUP BY 
    p.Gender,
    p.Age
ORDER BY 
    FlightCount DESC;

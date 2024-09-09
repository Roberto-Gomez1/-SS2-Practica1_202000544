Use Seminario2
SELECT TOP 5
    a.CountryName AS Country,
    COUNT(v.HechoID) AS FlightCount
FROM 
    Vuelo v
JOIN 
    Aeropuerto a ON v.ArrivalAirportID = a.ArrivalAirportID
GROUP BY 
    a.CountryName
ORDER BY 
    FlightCount DESC;

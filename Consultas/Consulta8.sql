Use Seminario2
SELECT TOP 5
    a.AirportContinent AS Continent,
    COUNT(v.HechoID) AS FlightCount
FROM 
    Vuelo v
JOIN 
    Aeropuerto a ON v.ArrivalAirportID = a.ArrivalAirportID
GROUP BY 
    a.AirportContinent
ORDER BY 
    FlightCount DESC;

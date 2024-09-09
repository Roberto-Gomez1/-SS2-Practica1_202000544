Use Seminario2
SELECT 
    a.CountryName AS Country,
    COUNT(*) AS FlightCount
FROM 
    Vuelo v
JOIN 
    Aeropuerto a ON v.ArrivalAirportID = a.ArrivalAirportID
GROUP BY 
    a.CountryName
ORDER BY 
    FlightCount DESC;

Use Seminario2
SELECT TOP 5
    a.AirportName,
    COUNT(v.PassengerID) AS PassengerCount
FROM 
    Vuelo v
JOIN 
    Aeropuerto a ON v.ArrivalAirportID = a.ArrivalAirportID
GROUP BY 
    a.AirportName
ORDER BY 
    PassengerCount DESC;

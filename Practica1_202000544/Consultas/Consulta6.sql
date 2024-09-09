Use Seminario2
SELECT TOP 3
    FlightStatus AS Status,
    COUNT(*) AS FlightCount
FROM 
    Vuelo
GROUP BY 
    FlightStatus
ORDER BY 
    FlightCount DESC;

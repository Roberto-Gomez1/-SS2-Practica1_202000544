Use Seminario2
SELECT 
    FORMAT(v.DepartureDate, 'MM-yyyy') AS MonthYear,
    COUNT(v.HechoID) AS FlightCount
FROM 
    Vuelo v
GROUP BY 
    FORMAT(v.DepartureDate, 'MM-yyyy')
ORDER BY 
    MonthYear;

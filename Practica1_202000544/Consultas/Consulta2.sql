Use Seminario2
SELECT 
    Gender,
    COUNT(*) AS TotalByGender,
    (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Pasajero)) AS Percentage
FROM 
    Pasajero
GROUP BY 
    Gender;

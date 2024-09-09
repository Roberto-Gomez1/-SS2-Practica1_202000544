USE Seminario2;

WITH MonthlyFlightCounts AS (
    SELECT 
        p.Nationality,
        FORMAT(v.DepartureDate, 'MM-yyyy') AS MonthYear,
        COUNT(v.HechoID) AS FlightCount
    FROM 
        Vuelo v
    JOIN 
        Pasajero p ON v.PassengerID = p.PassengerID
    GROUP BY 
        p.Nationality,
        FORMAT(v.DepartureDate, 'MM-yyyy')
),
MaxMonthlyFlights AS (
    SELECT
        Nationality,
        MAX(FlightCount) AS MaxFlightCount
    FROM
        MonthlyFlightCounts
    GROUP BY
        Nationality
)
SELECT
    m.Nationality,
    m.MonthYear,
    m.FlightCount
FROM
    MonthlyFlightCounts m
JOIN
    MaxMonthlyFlights maxf
    ON m.Nationality = maxf.Nationality
    AND m.FlightCount = maxf.MaxFlightCount
ORDER BY
    m.Nationality,
    m.MonthYear;

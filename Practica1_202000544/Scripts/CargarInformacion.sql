

INSERT INTO Pasajero (PassengerID, FirstName, LastName, Gender, Age, Nationality)
SELECT DISTINCT 
    t.PassengerID, 
    t.FirstName, 
    t.LastName, 
    t.Gender, 
    TRY_CAST(t.Age AS INT), 
    t.Nationality
FROM 
    (SELECT 
         PassengerID, 
         MIN(FirstName) AS FirstName, 
         MIN(LastName) AS LastName, 
         MIN(Gender) AS Gender, 
         MIN(Age) AS Age, 
         MIN(Nationality) AS Nationality
     FROM Temporal
     GROUP BY PassengerID) t
WHERE NOT EXISTS (
    SELECT 1 
    FROM Pasajero p 
    WHERE p.PassengerID = t.PassengerID
);

select count(*) from Pasajero

INSERT INTO Aeropuerto (ArrivalAirportID, AirportName, AirportCountryCode, CountryName, AirportContinent)
SELECT DISTINCT 
    t.ArrivalAirport,
    t.AirportName,
    t.AirportCountryCode,
    t.CountryName,
    t.AirportContinent
FROM 
    (SELECT 
         ArrivalAirport,
         MIN(AirportName) AS AirportName, 
         MIN(AirportCountryCode) AS AirportCountryCode, 
         MIN(CountryName) AS CountryName, 
         MIN(AirportContinent) AS AirportContinent
     FROM Temporal
     GROUP BY ArrivalAirport) t
WHERE NOT EXISTS (
    SELECT 1 
    FROM Aeropuerto a 
    WHERE a.ArrivalAirportID = t.ArrivalAirport
);

select count(*) from Aeropuerto


INSERT INTO Piloto (PilotName)
SELECT DISTINCT 
    t.PilotName
FROM 
    (SELECT 
         PilotName
     FROM Temporal
     GROUP BY PilotName) t
WHERE NOT EXISTS (
    SELECT 1 
    FROM Piloto p 
    WHERE p.PilotName = t.PilotName
);

select count(*) from Piloto


INSERT INTO Vuelo (PassengerID, FlightStatus, DepartureDate, ArrivalAirportID, PilotID)
SELECT 
    t.PassengerID,
    t.FlightStatus,
    TRY_CAST(t.DepartureDate AS DATE),
    a.ArrivalAirportID,
    p.PilotID
FROM Temporal t
JOIN Aeropuerto a ON t.ArrivalAirport = a.ArrivalAirportID
JOIN Piloto p ON t.PilotName = p.PilotName;


SELECT COUNT(*) FROM Vuelo;

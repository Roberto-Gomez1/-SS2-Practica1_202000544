USE Seminario2

CREATE TABLE Temporal (
    PassengerID VARCHAR(50),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(50),
    Age VARCHAR(50),
    Nationality VARCHAR(50),
    AirportName VARCHAR(100),
    AirportCountryCode VARCHAR(50),
    CountryName VARCHAR(100),
    AirportContinent VARCHAR(50),
    Continents VARCHAR(100),
    DepartureDate VARCHAR(50),
    ArrivalAirport VARCHAR(100),
    PilotName VARCHAR(100),
    FlightStatus VARCHAR(50)
);

CREATE TABLE Pasajero (
    PassengerID VARCHAR(50) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(50),
    Age INT,
    Nationality VARCHAR(50)
);

CREATE TABLE Aeropuerto (
    ArrivalAirportID VARCHAR(50) PRIMARY KEY,
    AirportName VARCHAR(100),
    AirportCountryCode VARCHAR(50),
    CountryName VARCHAR(100),
    AirportContinent VARCHAR(50)
);

CREATE TABLE Piloto (
    PilotID INT PRIMARY KEY IDENTITY(1,1),
    PilotName VARCHAR(100)
);

CREATE TABLE Vuelo (
    HechoID INT PRIMARY KEY IDENTITY(1,1),
    PassengerID VARCHAR(50),
    FlightStatus VARCHAR(50),
    DepartureDate DATE,
    ArrivalAirportID VARCHAR(50),
    PilotID INT,
    FOREIGN KEY (PassengerID) REFERENCES Pasajero(PassengerID),
    FOREIGN KEY (ArrivalAirportID) REFERENCES Aeropuerto(ArrivalAirportID),
    FOREIGN KEY (PilotID) REFERENCES Piloto(PilotID)
);

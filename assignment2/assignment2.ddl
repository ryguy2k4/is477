CREATE TABLE Airline1_Schedule(
    FlightId NUMBER,
    FlightNumber NUMBER,
    StartDate TEXT,
    EndDate TEXT,
    DepartureTime TEXT,
    DepartureAirport TEXT,
    ArrivalTime TEXT,
    ArrivalAirport TEXT,
    PRIMARY KEY (FlightId)
);

CREATE TABLE Airline1_Flight(
    FlightId NUMBER,
    DepartureDate TEXT,
    DepartureTime TEXT,
    DepartureGate TEXT,
    ArrivalDate TEXT,
    ArrivalTime TEXT,
    ArrivalGate TEXT,
    PlaneId NUMBER,
    PRIMARY KEY (DepartureDate),
    FOREIGN KEY (FlightID) REFERENCES Airline1_Schedule(FlightId)
);

CREATE TABLE Airline2_Flight(
    FlightNumber NUMBER,
    DepartureAirport TEXT,
    ScheduledDepartureDate TEXT,
    ScheduledDepartureTime TEXT,
    ActualDepartureTime TEXT,
    ArrivalAirport TEXT,
    ScheduledArrivalDate TEXT,
    ScheduledArrivalTime TEXT,
    ActualArrivalTime TEXT,
    PRIMARY KEY (FlightNumber, DepartureAirport, ScheduledDepartureDate)
);

CREATE TABLE Airport3_Arrivals(
    Airline TEXT,
    FlightNumber NUMBER,
    Scheduled TEXT,
    Actual TEXT,
    GateTime TEXT,
    LandingTime TEXT,
    Terminal TEXT,
    Gate NUMBER,
    Runway NUMBER,
    PRIMARY KEY (FlightNumber, Airline, Scheduled)
);

CREATE TABLE Airport3_Departures(
    Airline TEXT,
    FlightNumber NUMBER,
    Scheduled TEXT,
    Actual TEXT,
    GateTime TEXT,
    TakeoffTime TEXT,
    Terminal TEXT,
    Gate NUMBER,
    Runway NUMBER,
    PRIMARY KEY (FlightNumber, Airline, Scheduled)
);

CREATE TABLE Airfare4_Flight(
    FlightId NUMBER,
    FlightNumber TEXT,
    DepartureAirport TEXT,
    DepartureDate TEXT,
    DepartureTime TEXT,
    ArrivalAirport TEXT,
    ArrivalTime TEXT,
    PRIMARY KEY (FlightId)
);

CREATE TABLE Airfare4_Fares(
    FlightId NUMBER,
    FareClass TEXT,
    Fare NUMBER,
    PRIMARY KEY (FareClass, Fare),
    FOREIGN KEY (FlightId) REFERENCES Airfare4_Flight(FlightId)
);

CREATE TABLE Airinfo5_AirportCodes(
    AirportCode TEXT,
    AirportName TEXT,
    PRIMARY KEY (AirportCode)
);

CREATE TABLE Airinfo5_AirlineCodes(
    AirlineCode TEXT,
    AirlineName TEXT,
    PRIMARY KEY (AirlineCode)
);
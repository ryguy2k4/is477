CREATE TABLE lab6_flights(
    Airline TEXT,
    FlightNumber NUMBER,
    DepartureAirport TEXT,
    ScheduledDepartureDate Text,
    ScheduledDepartureTime Text,
    ActualDepartureTime Text,
    ArrivalAirport Text,
    ScheduledArrivalDate Text,
    ScheduledArrivalTime Text,
    ActualArrivalTime Text,
    PRIMARY KEY (airline, flightNumber, departureAirport, scheduledDepartureDate)
);
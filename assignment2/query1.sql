SELECT s.FlightNumber as FlightNumber, s.ArrivalAirport as ArrivalAirport, f.ArrivalGate as ArrivalGate
FROM Airline1_Flight as f, Airline1_Schedule as s
WHERE s.FlightId = f.FlightId;
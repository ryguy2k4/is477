SELECT a.Airline as Airline, a.FlightNumber as FlightNumber, 'EWR' as ArrivalAirport, a.Terminal || a.Gate as ArrivalGate
FROM Airport3_Arrivals as a

UNION

SELECT b.Airline as Airline, b.FlightNumber as FlightNumber, NULL as ArrivalAirport, b.Terminal || b.Gate as ArrivalGate
FROM Airport3_Departures as b
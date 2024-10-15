INSERT INTO Integrated_Arrival

SELECT 'A1' as Airline, 
        b.FlightNumber as FlightNumber,
        a.ArrivalDate as ScheduledArrivalDate, 
        c.Actual as ActualArrivalDate, 
        b.ArrivalTime as ScheduledArrivalTime,
        a.ArrivalTime as ActualArrivalTime, 
        c.GateTime as GateTime, 
        c.LandingTime as LandingTime,
        a.ArrivalGate as ArrivalGate

FROM Airline1_Flight as a

JOIN Airline1_Schedule as b 
ON a.FlightId = b.FlightId

JOIN Airport3_Arrivals as c 
ON 'EWR' = b.ArrivalAirport
AND 'A1' = c.Airline 
AND b.FlightNumber = c.FlightNumber 
AND a.ArrivalDate = c.Scheduled 
;
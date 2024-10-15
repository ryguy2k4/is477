INSERT INTO Integrated_Arrival

SELECT 'A2' as Airline, 
        a.FlightNumber as FlightNumber,
        a.ScheduledArrivalDate as ScheduledArrivalDate, 
        c.Actual as ActualArrivalDate, 
        a.ScheduledArrivalTime as ScheduledArrivalTime,
        a.ActualArrivalTime as ActualArrivalTime, 
        c.GateTime as GateTime, 
        c.LandingTime as LandingTime,
        c.Terminal || c.Gate as ArrivalGate

FROM Airline2_Flight as a

JOIN Airport3_Arrivals as c 
ON 'EWR' = a.ArrivalAirport
AND 'A2' = c.Airline 
AND a.FlightNumber = c.FlightNumber 
AND a.ScheduledArrivalDate = c.Scheduled 
;
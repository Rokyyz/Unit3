## quiz_050

# 1. UML Diagram

![CommSci 34](https://github.com/Rokyyz/Unit3/assets/134658259/d4e7f74d-f2ac-44bb-a570-c1bc40e4a95a)

# 2. Solution

```.py

class Flights():
    def __init__(self, flight_number:str, origin:str, destination:str, departure_time:str, duration:list[int]):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.duration = duration



    def get_duration(self, duration,destination):
        h = duration[0]
        m = duration[1]
        s = duration[2]
        return f"to {destination} which lasts {h} hours {m} minutes {s} seconds"

first = Flights(flight_number = "LV199", origin = "Riga", destination = "Dream Airport", departure_time = "5.00 AM",duration = [10, 57, 12])
second= Flights(flight_number = "SU66", origin = "Osaka", destination = "Mocks International Airport", departure_time = "6.45 AM",duration = [1, 40, 35])

final1 = (first.get_duration(duration = second.duration,destination=second.destination))
final2 = (second.get_duration(duration = first.duration,destination=first.destination))

print(f"Our airline offers a flight from ISAK {final1}")
print(f"Our airline also offers a flight from ISAK {final2}")

```

# 3. Proof of work
<img width="1440" alt="Screenshot 2024-02-20 at 19 38 34" src="https://github.com/Rokyyz/Unit3/assets/134658259/b6110e1c-4555-4014-ace7-32ed57419296">

# 4. For fun 
```.py
class Flights():
    def __init__(self, flight_number:str, origin:str, destination:str, departure_time:str, duration:list[int]):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.duration = duration



    def get_duration(self, duration,destination):
        h = duration[0]
        m = duration[1]
        s = duration[2]
        return f"to {destination}. Your flight length is {h} hours {m} minutes {s} seconds"

    def get_flight_number(self, flight_number:str, origin: str, departure_time:str):
        flight1 = flight_number
        origin1 = origin
        departure_time1 = departure_time
        return f"from {origin1}.\nYour flight number is {flight1} and departs at {departure_time1}, it goes to"


first = Flights(flight_number = "LV199", origin = "Riga", destination = "Dream Airport", departure_time = "5.00 AM",duration = [10, 57, 12])
second= Flights(flight_number = "SU66", origin = "Osaka", destination = "Mocks International Airport", departure_time = "6.45 AM",duration = [1, 40, 35])

final1 = (first.get_duration(duration = second.duration,destination=second.destination))
final2 = (second.get_duration(duration = first.duration,destination=first.destination))

message1 = (first.get_flight_number(flight_number=second.flight_number, origin=second.origin, departure_time=second.departure_time))
message2 = (first.get_flight_number(flight_number=first.flight_number, origin=first.origin, departure_time=first.departure_time))

print(f"Our airline offers a flight {message1} {final1}")
print(f"Our airline also offers a flight from {message2} {final2}")

```

<img width="1440" alt="Screenshot 2024-02-20 at 22 49 00" src="https://github.com/Rokyyz/Unit3/assets/134658259/501461a8-862a-4a79-bad2-4d8a5d16dc00">


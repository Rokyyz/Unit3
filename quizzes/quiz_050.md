## quiz_050

1. UML Diagram

![CommSci 34](https://github.com/Rokyyz/Unit3/assets/134658259/d4e7f74d-f2ac-44bb-a570-c1bc40e4a95a)

2. Solution

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

3. Proof of work
<img width="1440" alt="Screenshot 2024-02-20 at 19 38 34" src="https://github.com/Rokyyz/Unit3/assets/134658259/b6110e1c-4555-4014-ace7-32ed57419296">


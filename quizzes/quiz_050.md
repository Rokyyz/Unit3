## quiz_050

1. Diagram


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
        hours = duration[0]
        minutes = duration[1]
        seconds = duration[2]
        return f"{hours} hours {minutes} minutes {seconds} seconds remaining for {destination}"

first = Flights(flight_number = "CA908", origin = "Madrid", destination = "Beijing International Airport", departure_time = "11.30 AM",duration = [10, 57, 12])
second= Flights(flight_number = "IB64", origin = "Madrid", destination = "Bilbao Airport", departure_time = "8.30 AM",duration = [1, 40, 35])

print(first.get_duration(duration = second.duration,destination=second.destination))

print(second.get_duration(duration = first.duration,destination=first.destination))

```

3. Proof of work

<img width="1440" alt="Screenshot 2024-02-19 at 22 13 57" src="https://github.com/Rokyyz/Unit3/assets/134658259/1da86abe-0a41-45cf-9687-4cf425323559">

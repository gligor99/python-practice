class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(10,12)
print(p1.x, p1.y)

class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity;
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():   # if self.open_seats === 0;
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
#print(flight.capacity)

people = ['Luka', "Marko", 'Luka2', "Marko2"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"Not avaliable seats for {person}")
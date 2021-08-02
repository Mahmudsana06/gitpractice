print("Here I have attached a program learnt from CS50 in which we can add passenger's name if there is an empty seat in the airplane.")
class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passenger=[]
    
    def add_passenger(self,name): 
        if not self.empty_seat():
            return False
        self.passenger.append(name)
        return True
    
    def empty_seat(self):
        return self.capacity - len(self.passenger)

flight=Flight(3)

people=["A","B","C","D","E"]

for i in people:
    success = flight.add_passenger(i)

    if success:
        print(f"Adding {i} is successful.")
    else:
        print(f"{i} cannot be")
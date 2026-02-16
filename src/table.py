class Seat: 

    def __init__(self): 
        self.free = True
        self.occupant = ""

    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False
        else: 
            print("Seat is already taken")

    def remove_occupant(self):
        if not self.free: 
            name = self.occupant
            self.occupant = ""
            self.free = True 
            return name
        else:
            print("Seat is emtpy.")
            


class Table: 

    def __init__(self):
        self.capacity = 4
        self.seats = [Seat() for _ in range(self.capacity)] 
        # Each time the loop runs a NEW Seat object is created
        """ [Seat(), Seat(), Seat(), Seat()]"""
        """ Table
        ├─ capacity = 4
        └─ seats = [
              Seat(free=True, occupant=""),
               Seat(free=True, occupant=""),
               Seat(free=True, occupant=""),
               Seat(free=True, occupant="")
               ] """
    
    def has_free_spot(self): # Does this table have free seats?
        if self.left_capacity() > 0: 
            return True 
        else: 
            return False
                   
    def assign_seat(self, name): 
        for seat in self.seats: # Loops through each Seat() object
            if seat.free: 
                 seat.set_occupant(name)
                 break # --> Without break, ALL free seats with the same name

    def left_capacity(self): # how many seats are still free
        free_seat = 0 
        for seat in self.seats: 
            if seat.free: 
                free_seat += 1 
        return free_seat

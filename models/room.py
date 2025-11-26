
class Room:
    def __init__(self,number):
        self.number = number
        self.sleeping_places = []


    def add_bed(self,soldier:"Soldier"):
        if len(self.sleeping_places) < 8:
            self.sleeping_places.append(soldier)
            return True
        return False

    def is_full(self):
        return len(self.sleeping_places) == 8





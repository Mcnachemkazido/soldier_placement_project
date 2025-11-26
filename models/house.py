
class House:
    def __init__(self,name):
        self.name = name
        self.rooms = []

    def add_room(self,room:"Room"):
        if len(self.rooms) < 10:
            self.rooms.append(room)
            return True
        return False

    def is_full(self):
        return len(self.rooms) == 10

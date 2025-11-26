from soldier import Soldier
from room import Room
from house import House


class Management:
    def __init__(self,list_of_soldiers):
        self.list_of_soldiers = list_of_soldiers

    def to_fill_a_first_house(self):
        full_houses = []
        houses = ["Dorm_A" ,"Dorm_B"]
        for h in houses:
            house = House(h)
            room_count = 1
            while not (house.is_full()) and self.list_of_soldiers:
                room = Room(room_count)
                house.add_room(room)
                room_count += 1
                while not(room.is_full()) and self.list_of_soldiers:
                    room.add_bed(self.list_of_soldiers.pop())
            full_houses.append(house)
        return full_houses , self.list_of_soldiers



x = [i for i in range(1000)]
m = Management(x)
h = m.to_fill_a_first_house()
print(h)
for i in h[0]:
    x = i.rooms
    for j in x:
        print(j.sleeping_places)
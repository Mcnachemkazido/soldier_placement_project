from soldier import Soldier
from room import Room
from house import House


class Management:
    def __init__(self,list_of_soldiers):
        self.list_of_soldiers = list_of_soldiers

    def fill_the_houses(self):
        full_houses = []
        houses = ["Dorm_A" ,"Dorm_B"]
        for h in houses:
            house = House(h)
            room_count = 1
            while not (house.is_full()) and self.list_of_soldiers:
                room = Room(room_count)
                room_count += 1
                while not(room.is_full()) and self.list_of_soldiers:
                    room.add_bed(self.list_of_soldiers.pop())
                house.add_room(room)
            full_houses.append(house)
        return full_houses , self.list_of_soldiers

#
# s2 = Soldier(1,2,4,56,5)
# s1 = Soldier(1,2,4,56,5)
# m= Management([s1,s2])
# f = m.fill_the_houses()
# print(f[0][0].is_full())
# #
# x = [i for i in range(200)]
# m = Management(x)
# f = m.fill_the_houses()
# print(f[0][0].rooms[0].sleeping_places)
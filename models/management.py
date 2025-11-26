from models.room import Room
from models.house import House



class Management:
    def __init__(self,list_of_soldiers):
        self.list_of_soldiers = list_of_soldiers
        self.placement_list = []

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
                    soldier = self.list_of_soldiers.pop()
                    soldier.placement_details["house"] = house.name
                    soldier.placement_details["room"] =room.number
                    soldier.is_it_placed = True
                    room.add_bed(soldier)
                    self.placement_list.append(soldier)
                house.add_room(room)
            full_houses.append(house)

    def soldier_deployment_details(self):
        already = []
        waiting_list = []

        for s in self.placement_list:
            already.append({"name":s.name,"is_it_placeds":s.is_it_placed,
                            "Placement details":s.placement_details})

        for s in self.list_of_soldiers:
            waiting_list.append({"name":s.name,"is_it_placeds":s.is_it_placed,
                            "Placement details":"waiting list"})



        return {"amount of placement":len(self.placement_list),
                "waiting_list":len(self.list_of_soldiers),
                "Soldiers_who_were_deployed":already,
                "Soldiers waiting":waiting_list
                }



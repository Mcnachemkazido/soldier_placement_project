
class Soldier:
    def __init__(self,personal_number:int,name:str,family:str,gender:str,city:str,distance:int):
            self.personal_number = personal_number
            self.name = name
            self.family = family
            self.gender = gender
            self.city = city
            self.distance = distance
            self.is_it_placed = False
            self.placement_details = {"house":False,"room":False}



     # if isinstance(personal_number,int) and str(personal_number)[0] == '8':
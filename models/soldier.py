
class Soldier:
    def __init__(self,personal_number:int,name:str,family:str,city:str,distance:int):
        if isinstance(personal_number,int) and str(personal_number)[0] == '8':
            self.personal_number = personal_number
            self.name = name
            self.family = family
            self.city = city
            self.distance = distance
            self.is_it_placed = False
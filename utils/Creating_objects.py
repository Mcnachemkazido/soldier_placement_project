from models.soldier import Soldier


def creating_soldier_objects(list_of_soldiers):
    list_of_objects = []
    for s in list_of_soldiers:
        if s[0][0] == "8" and all(char.isdigit() for char in s[0]):
            objects = Soldier(s[0], s[1], s[2], s[3], s[4], s[5])
            list_of_objects.append(objects)
    return list_of_objects



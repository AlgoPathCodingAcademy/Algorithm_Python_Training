'''
Complete the constructor of character class,
so that it runs and prints the following:
Name:  Aragon  Position:x  100  Position:y  200  Hp  150
'''

class NameComponent:
    def __init__(self, name):
        self.name = name

class PositionComponent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class HealthComponent:
    def __init__(self, hp):
        self.hp = hp

class Character:
    def __init__(self, name, x, y, hp):
        pass
        
    def display_info(self):
        print("Name: ", self.name_component.name, 
            " Position:x ", self.position_component.x,
            " Position:y ", self.position_component.y,
            " Hp ", self.health_component.hp)

# Create a character instance
character = Character('Aragon', 100, 200, 150)

# Call method to display character information
character.display_info()


'''
Task:
Refactor the code to remove the inheritance relationship.
Instead, use composition to give a Photographer access to Camera functionality.

class Camera:
    def record(self):
        print("Recording video.")

class Photographer(Camera):
    pass

photographer = Photographer()
photographer.record() # Works, but conceptually incorrect.
'''

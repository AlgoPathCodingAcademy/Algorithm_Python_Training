'''
Change the following code using Encapsulation so that
it only exposes the information it really needs to
'''
class Character:
    def __init__(self):
        self.item1 = None
        self.item2 = None

    def show_inventory(self):
        print("Items are ", self.item1, " and ", self.item2)
   
    def setItem1(self, item1):
        self.item1 = item1
        
    def setItem2(self, item2):
        self.item2 = item2

# Example usage:
hero = Character()
hero.setItem1("Sword")
hero.setItem2("Shield")
hero.show_inventory()

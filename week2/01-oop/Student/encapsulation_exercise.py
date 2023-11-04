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

# Example usage:
hero = Character()
hero.item1 = "Sword"  # Directly setting the attribute
hero.item2 = "Shield"  # Directly setting the attribute
hero.show_inventory()

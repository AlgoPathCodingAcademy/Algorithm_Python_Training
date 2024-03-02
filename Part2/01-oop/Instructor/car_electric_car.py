class my_car:
    def __init__(self,model,color,safeToDrive):
        self.model = model
        self.color = color
        self.safeToDrive = safeToDrive
   
    def showMeYourColor(self):
        print("Ok, color is ", self.color)
   
    def isOkToDrive(self):
        if (self.safeToDrive):
            print("Safe to Drive")
        else:
            print("No")


class my_electrical_car(my_car):
    def __init__(self, model, color, safeToDrive, battery_power):
        super().__init__(model, color, safeToDrive)
        self.battery_power = battery_power
        
    def getBatteryPower(self):
        return self.battery_power
        
    def setBatteryPower(self, power):
        self.battery_power = power
        
    def refuel(self):
        print("Recharging the ", self.model ,"'s battery")

class my_car_aliases(my_car):
    pass
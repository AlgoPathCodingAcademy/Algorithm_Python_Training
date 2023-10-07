#Class basic
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
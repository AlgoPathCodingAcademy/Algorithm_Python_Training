import car
import car_electric_car
#print(car.__file__)
my_car_object = car.my_car("audi","orange",False)
my_car_object.isOkToDrive()

my_electric_car_object = car_electric_car.my_car("bmw","blue",True)
my_electric_car_object.isOkToDrive()

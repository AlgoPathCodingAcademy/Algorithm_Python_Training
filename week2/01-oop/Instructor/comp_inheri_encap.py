class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.temperature = 0

    def start(self):
        self.temperature = 60

    def stop(self):
        self.temperature = 0

# Inappropriate inheritance
class Car(Engine):  # Inheriting from Engine, but a Car is not a type of Engine
    def __init__(self, fuel_type, model):
        super().__init__(fuel_type)
        self.model = model

    def get_engine_temperature(self):
        return self.temperature

# Usage
my_car = Car("Petrol", "XYZ123")
my_car.start()
print(f"The engine temperature is {my_car.get_engine_temperature()} degrees.")


'''
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.temperature = 0

    def start(self):
        self.temperature = 60

    def stop(self):
        self.temperature = 0

class Car:
    def __init__(self, fuel_type, model):
        self.engine = Engine(fuel_type)  # Composition
        self.model = model

    def get_engine_temperature(self):
        return self.engine.temperature

# Usage
my_car = Car("Petrol", "XYZ123")
my_car.engine.start()
print(f"The engine temperature is {my_car.get_engine_temperature()} degrees.")
'''

'''

'''
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.temperature = 0  # Private attribute

    def start(self):
        self.temperature = 200

    def stop(self):
        self.temperature = 0

    def get_temperature(self):
        return self.temperature  # Proper encapsulation

class Car:
    def __init__(self, fuel_type, model):
        self.engine = Engine(fuel_type)  # Composition
        self.model = model

    def get_engine_temperature(self):
        return self.engine.get_temperature()  # Access through a public method of the composed Engine object

# Usage
my_car = Car("Petrol", "XYZ123")
my_car.engine.start()
print(f"The engine temperature is {my_car.get_engine_temperature()} degrees.")
'''

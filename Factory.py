from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass




class Car(Vehicle):

    def start_engine(self):
        print(f"{self.make} {self.model} : Двигун запущено")

class Motorcycle(Vehicle):
    
    def start_engine(self):
        print(f"{self.make} {self.model} : Мотор заведено")


class VehicleFactory(ABC):
    
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, f"{model} (USspec)")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (USspec)")
    

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, f"{model} (EUspec)")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (EUspec)")
    

def main():
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()

    vehicle1 = eu_factory.create_car("Euyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = us_factory.create_motorcycle("US-Davidson", "Sportster")
    vehicle2.start_engine()

if __name__ == "__main__":
    main()
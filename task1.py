from __future__ import annotations

import logging
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model

    @abstractmethod
    def start_engine(self) -> None: ...


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info("%s %s: Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info("%s %s: Мотор заведено", self.make, self.model)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car: ...

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle: ...


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} (EU Spec)")


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    
    us_factory: VehicleFactory = USVehicleFactory()
    eu_factory: VehicleFactory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()

    vehicle3 = eu_factory.create_car("Volkswagen", "Golf")
    vehicle3.start_engine()

    vehicle4 = us_factory.create_motorcycle("Indian", "Scout")
    vehicle4.start_engine()


if __name__ == "__main__":
    main()

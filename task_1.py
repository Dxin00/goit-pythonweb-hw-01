# from typing import List
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, region_spec: str) -> None:
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            "%s %s (%s Spec): Двигун запущено", self.make, self.model, self.region_spec
        )


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            "%s %s (%s Spec): Двигун запущено", self.make, self.model, self.region_spec
        )


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU")


def main() -> None:
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_car = us_factory.create_car("Hyundai", "Santafe")
    eu_car = eu_factory.create_car("ZAZ", "Slavuta")

    us_car.start_engine()
    eu_car.start_engine()


if __name__ == "__main__":
    main()

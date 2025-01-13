from abc import ABC, abstractmethod
from interfaces.chair_interfaces import Chair, VictorianChair, ModernChair
from interfaces.coffee_table_interface import CoffeeTable, VictorianCoffeeTable, ModernCoffeeTable
from interfaces.sofa_interface import Sofa, VictorianSofa, ModernSofa


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_coffe_table(self) -> CoffeeTable:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_coffe_table(self) -> CoffeeTable:
        return VictorianCoffeeTable()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_coffe_table(self) -> CoffeeTable:
        return ModernCoffeeTable()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

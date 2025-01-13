from abc import ABC, abstractmethod


class CoffeeTable(ABC):
    @abstractmethod
    def putOn(self):
        pass


class VictorianCoffeeTable(CoffeeTable):
    def putOn(self):
        print("Putting on VictorianCoffeeTable")


class ModernCoffeeTable(CoffeeTable):
    def putOn(self):
        print("Putting on ModernCoffeeTable")

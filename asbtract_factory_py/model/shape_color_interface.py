from abc import ABC, abstractmethod


class AbstractColor(ABC):
    @abstractmethod
    def color(self):
        pass


class Blue(AbstractColor):
    def color(self):
        print("Shape.blue")


class Red(AbstractColor):
    def color(self):
        print("Shape.red")

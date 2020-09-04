from abc import ABC, abstractmethod
from model.shape_size_interface import Small, Large
from model.shape_color_interface import Blue, Red


class ShapeFactory(ABC):
    @abstractmethod
    def set_size(self):
        pass

    @abstractmethod
    def set_color(self):
        pass


class SmallBlueCircleFactory(ShapeFactory):
    def set_size(self):
        return Small()

    def set_color(self):
        return Blue()


class LargeRedSquareFactory(ShapeFactory):
    def set_size(self):
        return Large()

    def set_color(self):
        return Red()

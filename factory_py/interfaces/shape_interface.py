from abc import ABC, abstractmethod


class IShape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(IShape):
    def draw(self):
        print("Circle.draw")


class Square(IShape):
    def draw(self):
        print("Square.draw")

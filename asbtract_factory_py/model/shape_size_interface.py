from abc import ABC, abstractmethod


class AbstractSize(ABC):
    @abstractmethod
    def size(self):
        pass


class Small(AbstractSize):
    def size(self):
        print("Shape.small")


class Large(AbstractSize):
    def size(self):
        print("Shape.large")

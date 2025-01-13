from abc import ABC, abstractmethod


class Sofa(ABC):
    @abstractmethod
    def sitOn(self):
        pass


class VictorianSofa(Sofa):
    def sitOn(self):
        print("Sitting on VictorianSofa")


class ModernSofa(Sofa):
    def sitOn(self):
        print("Sitting on ModernSofa")

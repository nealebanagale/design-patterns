from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def hasLegs(self):
        pass

    def sitOn(self):
        pass


class VictorianChair(Chair):
    def hasLegs(self):
        print("VictorianChair has legs")

    def sitOn(self):
        print("Sitting on VictorianChair")


class ModernChair(Chair):
    def hasLegs(self):
        print("ModernChair has no legs")

    def sitOn(self):
        print("Sitting on ModernChair")

from abc import ABC, abstractmethod


class ITransport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(ITransport):
    def deliver(self):
        print("Deliver by land in a box")
        # do something else


class Ship(ITransport):
    def deliver(self):
        print("Deliver by sea in a container")
        # do something else

from abc import ABC, abstractmethod
from interfaces.transport_interface import ITransport, Truck, Ship


class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> ITransport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return f"Logistics: {transport.deliver()}"


class RoadLogistics(Logistics):
    def create_transport(self) -> ITransport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> ITransport:
        return Ship()

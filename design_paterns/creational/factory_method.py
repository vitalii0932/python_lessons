from __future__ import annotations
from abc import ABC, abstractmethod



class DeliveryVehicle(ABC):
    @abstractmethod
    def delivery(self) -> str:
        pass

class Track(DeliveryVehicle):
    def delivery(self) -> str:
        return "... overland delivery ..."

class Ship(DeliveryVehicle):
    def delivery(self) -> str:
        return "... sea delivery ..."



class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def delivery(self) -> str:
        delivery_vehicle = self.factory_method()

        result = f"Creator: The same creator's code has just worked with {delivery_vehicle.delivery()}"

        return result

class TrackCreator(Creator):
    def factory_method(self) -> DeliveryVehicle:
        return Track()

class ShipCreator(Creator):
    def factory_method(self) -> DeliveryVehicle:
        return Ship()



def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.delivery()}", end="")


if __name__ == "__main__":
    print("App: Launched with the TrackCreator.")
    client_code(TrackCreator())
    
    print("\n")

    print("App: Launched with the ShipCreator.")
    client_code(ShipCreator())
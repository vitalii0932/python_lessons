from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractChair(ABC):
    @abstractmethod
    def sit(self) -> str:
        pass
    
class AbstractTable(ABC):
    @abstractmethod
    def put(self) -> str:
        pass
    

class ModernChair(AbstractChair):
    def sit(self) -> str:
        return "You can sit in a modern chair"

class OldChair(AbstractChair):
    def sit(self) -> str:
        return "You can sit in a old chair"


class ModernTable(AbstractTable):
    def put(self) -> str:
        return "You can put something on a modern table."

class OldTable(AbstractTable):
    def put(self) -> str:
        return "You can put something on a old table."



class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass

    @abstractmethod
    def create_table(self) -> AbstractTable:
        pass

class ModernFactory(AbstractFactory):
    def create_chair(self) -> AbstractChair:
        return ModernChair()

    def create_table(self) -> AbstractTable:
        return ModernTable()

class OldFactory(AbstractFactory):
    def create_chair(self) -> AbstractChair:
        return OldChair()

    def create_table(self) -> AbstractTable:
        return OldTable()



def client_code(factory: AbstractFactory) -> None:
    chair = factory.create_chair()
    table = factory.create_table()

    print(f"{chair.sit()}")
    print(f"{table.put()}")


if __name__ == "__main__":
    print("Client: Testing client code with the modern factory type:")
    client_code(ModernFactory())

    print("\n")

    print("Client: Testing the same client code with the old factory type:")
    client_code(OldFactory())
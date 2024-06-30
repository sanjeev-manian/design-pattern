from abc import ABC, abstractmethod


class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.window = None
        self.roof = None

    def __str__(self) -> str:
        return (
            f"House with {self.doors} doors, {self.walls} walls,"
            f"{self.roof} roof, {self.window} window"
        )


class HouseBuilder(ABC):
    @abstractmethod
    def build_walls():
        pass

    @abstractmethod
    def build_windows():
        pass

    @abstractmethod
    def build_doors():
        pass

    @abstractmethod
    def build_roof():
        pass


class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self, house=House()):
        self.house = house

    def build_walls(self):
        self.house.walls = "concrete walls"
        return self

    def build_doors(self):
        self.house.doors = "wood door"
        return self

    def build_windows(self):
        self.house.window = "glass window"
        return self

    def build_roof(self):
        self.house.roof = "concrete roof"
        return self

    def get_house(self):
        return self.house


class SandHouseBuilder(HouseBuilder):
    def __init__(self, house=House()):
        self.house = house

    def build_walls(self):
        self.house.walls = "Sand walls"
        return self

    def build_doors(self):
        self.house.doors = "iron door"
        return self

    def build_windows(self):
        self.house.window = "iron window"
        return self

    def build_roof(self):
        self.house.roof = "iron roof"
        return self

    def get_house(self):
        return self.house


cb = SandHouseBuilder()
print(cb.build_walls().build_doors().build_windows().build_roof().get_house())

from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def saying_hi(self):
        pass


class User(Person):
    def __init__(self, id: int, name: str) -> None:
        self.name = name
        self.id = id
        self.role = "user"

    def saying_hi(self):
        return f"name: {self.name}, id: {self.id}, role: {self.role}"


class Admin(Person):
    def __init__(self, id: int, name: str) -> None:
        self.name = name
        self.id = id
        self.role = "admin"

    def saying_hi(self):
        return f"name: {self.name}, id: {self.id}, role: {self.role}"


class PersonFactory(ABC):
    @abstractmethod
    def create_person(self, name: str) -> User:
        pass


class UserFactory(PersonFactory):
    def __init__(self) -> None:
        self.count = -1

    def create_person(self, name: str) -> User:
        self.count += 1
        return User(self.count, name)


class AdminFactory(PersonFactory):
    def __init__(self) -> None:
        self.count = -1

    def create_person(self, name: str) -> Admin:
        self.count += 1
        return Admin(self.count, name)


if __name__ == "__main__":
    uf = UserFactory()
    af = AdminFactory()
    print(uf.create_person("sanjeev").saying_hi())
    print(af.create_person("Kumar").saying_hi())
    print(uf.create_person("sanjeev").saying_hi())
    print(af.create_person("Kumar").saying_hi())

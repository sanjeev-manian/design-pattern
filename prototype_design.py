import copy


class Address:
    def __init__(self, street: str, suite: int, city: str) -> None:
        self.street = street
        self.suite = suite
        self.city = city


class Employee:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return (
            f"name: {self.name}, "
            f"Address : {self.address.street}, {self.address.suite}, {self.address.city}"
        )


class PrototypeFactory:
    main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
    aux_office_employee = Employee("", Address("46A west malabar", 0, "Delhi"))

    @staticmethod
    def __new_employee(prototype: Employee, name, suite) -> Employee:
        deep_copied_object = copy.deepcopy(prototype)
        deep_copied_object.name = name
        deep_copied_object.address.suite = suite
        return deep_copied_object

    @staticmethod
    def new_main_office_employee(name, suite) -> Employee:
        prototype = PrototypeFactory.main_office_employee
        return PrototypeFactory.__new_employee(prototype, name, suite)

    @staticmethod
    def new_aux_office_employee(name, suite) -> Employee:
        prototype = PrototypeFactory.aux_office_employee
        return PrototypeFactory.__new_employee(prototype, name, suite)


if __name__ == "__main__":
    uf = PrototypeFactory.new_aux_office_employee("sanjeev", 101)
    af = PrototypeFactory.new_main_office_employee("kumar", 201)
    print(uf)
    print(af)

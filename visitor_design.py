from abc import ABC, abstractmethod


# Visitor Interface
class Visitor(ABC):
    @abstractmethod
    def visit_element_a(self, element):
        pass

    @abstractmethod
    def visit_element_b(self, element):
        pass


# Concrete Visitor
class ConcreteVisitor(Visitor):
    def visit_element_a(self, element):
        print("Processing ElementA")

    def visit_element_b(self, element):
        print("Processing ElementB")


# Element Interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# Concrete Element A
class ElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)


# Concrete Element B
class ElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)


# Usage
def main():
    elements = [ElementA(), ElementB()]
    visitor = ConcreteVisitor()

    for element in elements:
        element.accept(visitor)


if __name__ == "__main__":
    main()

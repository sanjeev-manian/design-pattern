class Flyweight:
    def __init__(self, intrinsic_state):
        self.intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state):
        print(
            f"Intrinsic State: {self.intrinsic_state}, Extrinsic State: {extrinsic_state}"
        )


class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, key):
        if key not in self.flyweights:
            self.flyweights[key] = Flyweight(key)
        return self.flyweights[key]


# Client code
factory = FlyweightFactory()

# Shared flyweight
flyweight_a = factory.get_flyweight("A")
flyweight_a.operation("First Call")

# Reusing the same flyweight
flyweight_b = factory.get_flyweight("A")
flyweight_b.operation("Second Call")

# Different flyweight
flyweight_c = factory.get_flyweight("B")
flyweight_c.operation("Third Call")

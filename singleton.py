### 1. Classic Singleton using a Class Variable
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True


### 2. Singleton using a Decorator
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Singleton:
    pass


# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True


### 3. Singleton using a Metaclass
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True


### 5. Singleton using __init__ and __new__ Methods
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            # Perform initialization here
            self.initialized = True


# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True

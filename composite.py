from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, intent=0):
        pass


class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, intent=0):
        print(" " * intent + f"{self.name}")


class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self, intent=0):
        print(" " * intent + self.name + "/")
        for child in self.children:
            child.display(intent + 2)


root = Directory("root")
bin = Directory("bin")
usr = Directory("usr")
etc = Directory("etc")

root.add(bin)
root.add(usr)
root.add(etc)

bin.add(File("bash"))
bin.add(File("ls"))
bin.add(File("cat"))

usr.add(File("file1"))
usr.add(File("file2"))

etc.add(File("config1"))
etc.add(File("config2"))

root.display()

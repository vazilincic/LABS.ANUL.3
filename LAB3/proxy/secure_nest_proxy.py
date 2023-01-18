from lab3.proxy.nest import Nest


class SecureNestProxy (Nest):
    def __init__(self, nest):
        self.nest = nest

    def access(self, name):
        if (name == "TRex" or name == "Gigantosaurus"):
            print(f"{name} is not allowed to access the nest.")
        else:
            self.nest.access(name)

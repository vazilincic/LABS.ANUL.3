from lab3.proxy.nest import Nest


class RealNest (Nest):
    def access(self, name):
        print(f"{name} has access to the nest")

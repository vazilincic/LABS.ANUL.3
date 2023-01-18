from lab3.composite.plant import Plant


class Branch (Plant):
    def __init__(self, children):
        self.children = children

    def eat(self):
        for child in self.children:
            child.eat()

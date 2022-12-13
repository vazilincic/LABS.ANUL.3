from lab3.composite.plant import Plant


class Leaf(Plant):
    def __init__(self):
        self.IsEaten = False

    def eat(self):
        self.IsEaten = True
        print("Leaf eaten!")

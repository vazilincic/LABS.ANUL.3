from lab3.adapter.mammal import Mammal


class TriceratopsToMammalAdapter(Mammal):
    def __init__(self, triceratops):
        self.triceratops = triceratops

    def give_birth(self):
        egg = self.triceratops.lay_egg()
        child = egg.hatch()

        return child

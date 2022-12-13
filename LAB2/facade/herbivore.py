from lab3.facade.edible import Edible


class Herbivore (Edible):
    def __init__(self, plant):
        print("The herbivore eats a plant.")
        plant.eat()
        self.is_eaten = False

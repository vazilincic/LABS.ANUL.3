from lab3.facade.edible import Edible


class Carnivore (Edible):
    def __init__(self, herbivore):
        print("The carnivore eats the herbivore")
        herbivore.eat()
        self.is_eaten = False

    def die(self, soil):
        print("The carnivore dies")
        soil.add_nutrient(self)

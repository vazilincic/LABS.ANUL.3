from lab3.facade.plant import Plant
from lab3.facade.herbivore import Herbivore
from lab3.facade.carnivore import Carnivore


class DinoEcosystemFacade:
    def __init__(self, soil):
        self.soil = soil

    def run_a_generation(self):
        plant = Plant(self.soil)
        herbivore = Herbivore(plant)
        carnivore = Carnivore(herbivore)
        carnivore.die(self.soil)

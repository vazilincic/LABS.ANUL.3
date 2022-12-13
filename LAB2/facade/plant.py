from lab3.facade.edible import Edible


class Plant (Edible):
    def __init__(self, soil):
        print("A new plant grows")
        soil.use_nutrient()
        self.is_eaten = False

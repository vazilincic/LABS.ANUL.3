class Soil:
    def __init__(self, nutrient_count):
        self.nutrient_count = nutrient_count
        print(f"The soil has {self.nutrient_count} nutrient(s)")

    def add_nutrient(self, edible):
        print("The soil gains nutrients")
        edible.eat()
        self.nutrient_count += 1
        print(f"Nutrient count: {self.nutrient_count}")

    def use_nutrient(self):
        if (self.nutrient_count <= 0):
            print("No nutrients left!")
        self.nutrient_count -= 1
        print(f"Nutrient count: {self.nutrient_count}")

from lab4.strategy.eat_strategy import EatStrategy

class EatFastStrategy(EatStrategy):
    def eat(self, person):
        print(f"You have only {person.free_time} minutes, hurry up!")

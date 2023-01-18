from lab4.strategy.eat_strategy import EatStrategy


class EatSlowStrategy(EatStrategy):
    def eat(self, person):
        print("You have enough time, eat slowly.")

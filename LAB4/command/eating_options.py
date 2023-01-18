class EatingOptions:
    def __init__(self, eat_with_fork, eat_with_hands, eat_with_spoon):
        self.eat_with_fork = eat_with_fork
        self.eat_with_hands = eat_with_hands
        self.eat_with_spoon = eat_with_spoon

    def choose_fork(self):
        self.eat_with_fork.execute()

    def choose_hands(self):
        self.eat_with_hands.execute()

    def choose_spoon(self):
        self.eat_with_spoon.execute()

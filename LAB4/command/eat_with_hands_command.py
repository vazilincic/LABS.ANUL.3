from lab4.command.command_interface import Command


class EatWithHandsCommand(Command):
    def __init__(self, food):
        self.food = food

    def execute(self):
        self.food.eat_with_hands()

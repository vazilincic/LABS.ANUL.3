from lab3.decorator.abstract_gigantosaurus import AbstractGigantosaurus


class LoudGigantosarusDecorator (AbstractGigantosaurus):
    def __init__(self, gigantosaurus):
        self.gigantosaurus = gigantosaurus

    def roar(self):
        return f'{self.gigantosaurus.roar()} loudly'

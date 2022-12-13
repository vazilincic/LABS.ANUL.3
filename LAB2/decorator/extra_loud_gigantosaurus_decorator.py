from lab3.decorator.gigantosaurus import Gigantosaurus


class ExtraLoudGigantosaurusDecorator(Gigantosaurus):
    def __init__(self, gigantosaurus):
        self.gigantosaurus = gigantosaurus

    def roar(self):
        return f'{self.gigantosaurus.roar()}!'

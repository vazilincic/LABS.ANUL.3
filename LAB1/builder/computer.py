

from lab2.prototype.prototype import Prototype


class Computer(Prototype):
    def __init__(self):
        self.ram = None
        self.ram_price = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        info = ('RAM: {}GB, {}$'.format(self.ram, self.ram_price),
                'Storage: {}'.format(self.storage),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)

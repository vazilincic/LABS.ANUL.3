class HDD:
    def __init__(self):
        self.amount = 256
        self.model = 'Toshiba'
        self.price = '80$'

    def __str__(self):
        return f'{self.amount}GB, {self.model}, price: {self.price}'

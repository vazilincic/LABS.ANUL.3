class SSD:
    def __init__(self):
        self.amount = 256
        self.model = 'Kingston'
        self.price = '100$'

    def __str__(self):
        return f'{self.amount}GB, {self.model}, price: {self.price}'

class NvidiaGPUNew:
    def __init__(self):
        self.model = 'RTX 3090'
        self.price = '1000$'

    def __str__(self):
        return f'{self.model}, price: {self.price}'

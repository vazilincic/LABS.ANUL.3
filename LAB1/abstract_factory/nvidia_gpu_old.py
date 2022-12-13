class NvidiaGPUOld:
    def __init__(self):
        self.model = 'GTX 1080'
        self.price = '600$'

    def __str__(self):
        return f'{self.model}, price: {self.price}'

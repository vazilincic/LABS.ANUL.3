class Edible:
    def __init__(self):
        self.is_eaten = False

    def eat(self):
        if (self.is_eaten):
            print("Already eaten!")
        self.is_eaten = True

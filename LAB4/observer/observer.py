from lab4.observer.observer_interface import ObserverInterface


class Observer(ObserverInterface):
    def __init__(self, username, order):
        self.username = username
        order.add_observer(self)

    def update(self, availability):
        print(f"Hello {self.username}. You can let him leave the restaurant")

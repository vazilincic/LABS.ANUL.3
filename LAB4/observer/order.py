from lab4.observer.order_interface import OrderInterface


class Order(OrderInterface):
    def __init__(self, order_status, client_name):
        self.order_status = order_status
        self.client_name = client_name
        self.observers = []

    def get_order_status(self):
        return self.order_status

    def set_order_status(self, order_status):
        self.order_status = order_status
        self.notify_observers(order_status)

    def add_observer(self, observer):
        self.observers.append(observer)
        print(f"Added Observer: {observer.username}")

    def remove_observer(self, observer):
        self.observers.remove(observer)
        print(f"Observer Removed: {observer.username}")

    def notify_observers(self, order_status):
        if order_status == 'Order paid':
            print(
                f"Client has paid for the order, you can let {self.client_name} leave the restaurant")
        elif order_status == 'Order not paid':
            print(
                f"Client did not pay for the order, you can not let {self.client_name} leave the restaurant")
        for observer in self.observers:
            observer.update(self.order_status)

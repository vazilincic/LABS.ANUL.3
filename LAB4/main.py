from lab4.command.eat_with_fork_command import EatWithForkCommand
from lab4.command.eat_with_hands_command import EatWithHandsCommand
from lab4.command.eat_with_spoon_command import EatWithSpoonCommand
from lab4.command.eating_options import EatingOptions
from lab4.command.food import Food
from lab4.observer.order import Order
from lab4.observer.observer import Observer
from lab4.state.credit_card_machine import CreditCardMachine
from lab4.strategy.eat_strategy_selector import EatStrategySelector
from lab4.template.make_potato_burger import MakePotatoBurger
from lab4.template.make_chicken_burger import MakeChickenBurger
from lab4.person import Person

person = Person(name="Andrew", age=21, is_vegetarian=False, free_time=100)


print(f"Hi, my name is {person.name}")
print("I'm very hungry")
print()
print("(At the restaurant:)")

# Template
if (person.is_vegetarian):
    print("Hi. I want to eat a potato burger")
    print()
    print("(Chef in the kitchen:)")
    burger = MakePotatoBurger()
    burger.prepare()
else:
    print("Hi. I want to eat a chicken burger")
    print()
    print("(Chef in the kitchen:)")

    burger = MakeChickenBurger()
    burger.prepare()
# ----------


print("\nHow should I eat this burger?")
print("With fork, bare hands or spoon")

# Command
food = Food()
eatWithForkCommand = EatWithForkCommand(food)
eatWithHandsCommand = EatWithHandsCommand(food)
eatWithSpoonCommand = EatWithSpoonCommand(food)
eatingOptions = EatingOptions(
    eatWithForkCommand, eatWithHandsCommand, eatWithSpoonCommand)

print("Lets choose hands")

eatingOptions.choose_hands()
# ----------


print()
# Strategy
eatStrategySelector = EatStrategySelector()
eatStrategySelector.select_eat_strategy(person.free_time).eat(person)

person.free_time = 15
eatStrategySelector.select_eat_strategy(person.free_time).eat(person)
# ----------

print("\nLet's pay for the meal and go to work.")


# Observer
order = Order(order_status="Order not paid", client_name=person.name)
print(f"Order current status: {order.get_order_status()}")

print("3 guards arrived to stop you from leaving the restaurant without paying")

security1 = Observer("Alice", order)
security2 = Observer("Bob", order)
observers = Observer("Carol", order)
# ----------

print('\n')

# Observer
creditCardMachine = CreditCardMachine()

print("(credit Card Machine:)")
creditCardMachine.enter_pin()
creditCardMachine.eject_card()

creditCardMachine.insert_card()
creditCardMachine.enter_pin()

print()
order.set_order_status("Order paid")
# ----------

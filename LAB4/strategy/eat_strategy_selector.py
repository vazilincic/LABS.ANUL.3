from lab4.strategy.eat_strategy_selector_interface import EatStrategySelectorInterface
from lab4.strategy.eat_fast_strategy import EatFastStrategy
from lab4.strategy.eat_slow_strategy import EatSlowStrategy


class EatStrategySelector(EatStrategySelectorInterface):
    def select_eat_strategy(self, free_time):
        if free_time < 20:
            return EatFastStrategy()

        return EatSlowStrategy()

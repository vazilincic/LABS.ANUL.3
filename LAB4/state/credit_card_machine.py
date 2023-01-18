from lab4.state.credit_card_machine_state import CreditCardMachineState
from lab4.state.card_not_inserted_state import CardNotInsertedState
from lab4.state.card_inserted_state import CardInsertedState


class CreditCardMachine(CreditCardMachineState):

    def __init__(self):
        self.credit_card_machine_state = CardNotInsertedState()

    def insert_card(self):
        self.credit_card_machine_state.insert_card()
        if isinstance(self.credit_card_machine_state, CardNotInsertedState):
            self.credit_card_machine_state = CardInsertedState()

    def eject_card(self):
        self.credit_card_machine_state.eject_card()
        if isinstance(self.credit_card_machine_state, CardInsertedState):
            self.credit_card_machine_state = CardNotInsertedState()

    def enter_pin(self):
        return self.credit_card_machine_state.enter_pin()

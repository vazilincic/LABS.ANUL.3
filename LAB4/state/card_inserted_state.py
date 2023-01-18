from lab4.state.credit_card_machine_state import CreditCardMachineState

class CardInsertedState(CreditCardMachineState):
    def insert_card(self):
        print("Card already inserted")

    def eject_card(self):
        print("Card ejected")

    def enter_pin(self):
        print("Pin number has been entered correctly")
        print("Successful payment")
        return True

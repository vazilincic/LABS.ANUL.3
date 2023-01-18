from lab4.state.credit_card_machine_state import CreditCardMachineState


class CardNotInsertedState(CreditCardMachineState):
    def insert_card(self):
        print("Card Inserted")

    def eject_card(self):
        print("You cannot eject the card, there is no card inserted")

    def enter_pin(self):
        print("You cannot enter the pin, there is no card inserted")
        return False

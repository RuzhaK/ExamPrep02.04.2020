from project.card.card import Card

class CardRepository():
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card:Card):
        names=[x.name for x in self.cards]
        if card.name in names:
            raise ValueError(f"Card {card.name} already exists!")
        else:
            self.cards.append(card)
            self.count+=1

    def remove(self, card_name: str):
        if card_name=="":
            raise ValueError("Card cannot be an empty string!")
        else:

            card_to_remove=self.find(card_name)

            self.cards.remove(card_to_remove)
            self.count-=1


    def find(self, name: str):


        existing_card=[x for x in self.cards if x.name == name][0]

        return existing_card


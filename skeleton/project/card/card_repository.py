from project.card.card import Card

class CardRepository():
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card:Card):
        existing_card=[x for x in self.cards if x.name == card.name][0]
        if existing_card:
            raise ValueError(f"Card {card.name} already exists!")
        else:
            self.cards.append(card)
            self.count+=1

    def remove(self, card: str):
        if card=="":
            raise ValueError("Card cannot be an empty string!")
        else:
            existing_card = [x for x in self.cards if x.name == card][0]
            if existing_card:
                self.cards.remove(existing_card)
                self.count-=1

    def find(self, name: str):
        # todo tuk ne triabwa li da e s try?
        existing_card=[x for x in self.cards if x.name == name][0]
        if existing_card:
            return existing_card

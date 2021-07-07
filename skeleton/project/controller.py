from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller():
    def __init__(self):
        self.player_repository=PlayerRepository()
        self.card_repository=CardRepository()

    def add_player(self,type: str, username: str):
        type_to_check=type.lower()
        if type_to_check=="beginner":
            Beginner(username)
        elif type_to_check=="advanced":
            Advanced(username)
        else:
            return

        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self,type: str, name: str):
        type_to_check = type.lower()
        if type_to_check == "magic":
            MagicCard(name)
        elif type_to_check == "trap":
            TrapCard(name)
        else:
            return
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self,username: str, card_name: str):
        card=[card for card in self.card_repository.cards if card_name==card.name][0]
        user=[player for player in self.player_repository.players if player.username==username][0]
        if card and user:
            user.add_card(card)
            return f"Successfully added card: {card_name} to user: {username}"

    def fight(self,attack_name: str, enemy_name: str):
        attacker=[player for player in self.player_repository.players if player.username==attack_name][0]
        enemy=[player for player in self.player_repository.players if player.username==enemy_name][0]
        # todo ????
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result=''
        for player in self.player_repository.players:
            result+=f"Username: {player.username} - Health: {player.health} - Cards {len(player.card_repository.cards)}"
            for card in player.card_repository.cards:
                result+=f"### Card: {card.name} - Damage: {card.damage_points}"

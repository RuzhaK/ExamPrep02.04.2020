
from project.battle_field import BattleField
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

        if type=="Beginner":
            player=Beginner(username)
        elif type=="Advanced":
            player=Advanced(username)
        else:
            return
        self.player_repository.add(player)

        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self,type: str, name: str):

        if type == "Magic":
            card=MagicCard(name)
        elif type == "Trap":
            card=TrapCard(name)
        else:
            return
        self.card_repository.add(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self,username: str, card_name: str):
        card=[card for card in self.card_repository.cards if card_name==card.name][0]
        user=[player for player in self.player_repository.players if player.username==username][0]
        if card and user:
            user.card_repository.add(card)
            return f"Successfully added card: {card_name} to user: {username}"

    def fight(self,attack_name: str, enemy_name: str):
        try:
            attacker=[player for player in self.player_repository.players if player.username==attack_name][0]
            enemy=[player for player in self.player_repository.players if player.username==enemy_name][0]
            BattleField.fight(attacker,enemy)
            # todo taka si se izwikwa

            return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"
        except IndexError:
            pass



    def report(self):
        result=''
        for player in self.player_repository.players:
            result+=f"Username: {player.username} - Health: {player.health} - Cards {len(player.card_repository.cards)}\n"
            for card in player.card_repository.cards:
                result+=f"### Card: {card.name} - Damage: {card.damage_points}\n"
        return result

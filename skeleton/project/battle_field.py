from project.player.player import Player


class BattleField():
    def __init__(self):
        pass
    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            # todo tova gore moje da ne raboti s or
            raise ValueError("Player is dead!")
        # todo dolu
        if attacker.__class__.__name__=="Beginner":
            attacker.health+=40

            for card in attacker.card_repository.cards:
                card+=30

        self.get_bonus_health_points(attacker)
        self.get_bonus_health_points(enemy)

        for card in attacker.card_repository.cards:
            enemy.health-=card.damage_points
            if enemy.is_dead:
                return
        for card in enemy.card_repository.cards:
            attacker.health-=card.damage_points
            if attacker.is_dead:
                return





    def get_bonus_health_points(self, someone: Player):
        bonus=0
        for card in someone.card_repository.cards:
            bonus+=card.health_points
        someone.health+=bonus



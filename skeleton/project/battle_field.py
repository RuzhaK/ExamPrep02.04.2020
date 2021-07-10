from project.player.player import Player

class BattleField():
    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:

            raise ValueError("Player is dead!")

        if attacker.__class__.__name__=="Beginner":
            attacker.health+=40

            for card in attacker.card_repository.cards:
                card.damage_points+=30

        if enemy.__class__.__name__=="Beginner":
            enemy.health+=40

            for card in enemy.card_repository.cards:
                card.damage_points+=30

        get_bonus_health_points(attacker)
        get_bonus_health_points(enemy)

        for card in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return
            attacker.take_damage(card.damage_points)


def get_bonus_health_points(someone: Player):
    bonus=0
    for card in someone.card_repository.cards:
        bonus+=card.health_points
    someone.health+=bonus



from project.player.player import Player


class BattleField():
    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            # todo tova gore moje da ne raboti s or
            raise ValueError("Player is dead!")
        # todo dolu
        if attacker.__class__.__name__=="Beginner":
            attacker.health+=40

            for card in attacker.card_repository.cards:
                card.damage_points+=30
        if enemy.__class__.__name__=="Beginner":
            enemy.health+=40

            for card in enemy.card_repository.cards:
                card.damage_points+=30

        self.get_bonus_health_points(attacker)
        self.get_bonus_health_points(enemy)

        # for card in attacker.card_repository.cards:
        #     enemy.take_damage(card.damage_points)
        enemy.take_damage(attacker.total_damage())
        if enemy.is_dead:
            return
        # for card in enemy.card_repository.cards:
        #     attacker.take_damage(card.damage_points) 1:41
        # todo
        enemy.take_damage(attacker.total_damage())
        if attacker.is_dead:
            return




    @staticmethod
    def get_bonus_health_points( someone: Player):
        bonus=0
        for card in someone.card_repository.cards:
            bonus+=card.health_points
            someone.health+=bonus



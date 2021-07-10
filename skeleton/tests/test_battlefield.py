import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattler(unittest.TestCase):
    def test_fight_attacker_is_dead(self):
        a=Advanced('t')
        e=Advanced('t1')
        a.health=0

        with self.assertRaises(ValueError):
            BattleField.fight(a,e)

    def test_fight_enemy_is_dead(self):
        a=Advanced('t')
        e=Advanced('t1')
        e.health=0

        with self.assertRaises(ValueError):
            BattleField.fight(a,e)


    # def test_beginner_health_increases(self):
    #     a = Advanced('t')
    #     e = Advanced('t1')

    def test__health_increases(self):
        a = Advanced('t')
        e = Advanced('t1')

        card = TrapCard('t')
        a.card_repository.add(card)
        e.card_repository.add(card)

        self.assertEqual(a.health, 250)
        self.assertEqual(e.health, 250)

        BattleField.fight(a, e)

        self.assertEqual(a.health, 135)
        self.assertEqual(e.health, 135)

        self.assertFalse(a.is_dead)
        self.assertFalse(e.is_dead)

    def test__enemy_dies_in_battle(self):
        a = Advanced('t')
        e = Beginner('t1')

        card = TrapCard('t')
        card1 = TrapCard('t')
        a.card_repository.add(card)
        a.card_repository.add(card1)

        e.card_repository.add(card)

        self.assertEqual(a.health, 250)
        self.assertEqual(e.health, 50)
        with self.assertRaises(ValueError):
            BattleField.fight(a, e)

        self.assertEqual(a.health, 260)

        self.assertFalse(a.is_dead)
        self.assertTrue(e.is_dead)

    def test_health_increases(self):
        a = Advanced('t')
        e = Advanced('t1')

        card=TrapCard('t')
        a.card_repository.add(card)
        e.card_repository.add(card)

        self.assertEqual(a.health,250)
        self.assertEqual(e.health,250)

        BattleField.fight(a, e)

        self.assertEqual(a.health, 135)
        self.assertEqual(e.health, 135)

        self.assertFalse(a.is_dead)
        self.assertFalse(e.is_dead)

    def test_enemy_dies_in_battle(self):
        a = Advanced('t')
        e = Beginner('t1')

        card = TrapCard('t')
        card1 = TrapCard('t1')
        a.card_repository.add(card)
        a.card_repository.add(card1)

        e.card_repository.add(card)

        self.assertEqual(a.health, 250)
        self.assertEqual(e.health, 50)
        e.health+=175

        BattleField.fight(a,e)

        self.assertEqual(a.health, 260)

        self.assertEqual(e.health, 0)


        self.assertFalse(a.is_dead)
        self.assertTrue(e.is_dead)




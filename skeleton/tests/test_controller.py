import unittest

from project.battle_field import BattleField
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestController(unittest.TestCase):
    def test_init_controller(self):
        c=Controller()
        self.assertEqual(len(c.player_repository.players),0)
        self.assertEqual(len(c.card_repository.players),0)

    def test_add_player(self):
        c = Controller()
        res1=c.add_player("Beginner","A")
        res2=c.add_player("Advanced","C")

        self.assertEqual(res1,f"Successfully added player of type Beginner with username: A")
        self.assertEqual(res2,f"Successfully added player of type Advanced with username: C")

    def test_add_card(self):
        c = Controller()
        res1=c.add_card("Magic","A")
        res2=c.add_card("Trap","C")

        self.assertEqual(res1,f"Successfully added card of type MagicCard with name: A")
        self.assertEqual(res2,f"Successfully added card of type TrapCard with name: C")

    def test_add_player_card(self):
        c = Controller()
        c.add_player("Beginner","A")
        c.add_card("Trap","C")
        res=c.add_player_card("A","C")
        self.assertEqual(res,f"Successfully added card: C to user: A")

    def test_add_player_card(self):
        c = Controller()
        c.add_player("Beginner","A")
        c.add_card("Trap","C")
        res=c.add_player_card("A","C")
        self.assertEqual(res,f"Successfully added card: C to user: A")

    def test_fight(self):
        a = Advanced('t')
        e = Beginner('t1')
        c=Controller()
        c.player_repository.add(a)
        c.player_repository.add(e)
        res=c.fight("t","t1")


        self.assertEqual(res, f"Attack user health 250 - Enemy user health 90")

    def test_report(self):
        a = Advanced('t')
        e = Beginner('t1')
        c=Controller()
        c.player_repository.add(a)
        c.player_repository.add(e)
        res=c.report()


        self.assertEqual(res, "Username: t - Health: 250 - Cards 0\nUsername: t1 - Health: 50 - Cards 0\n")



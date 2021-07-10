import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestRepository(unittest.TestCase):
    def test_init_player_set_attributes(self):
        r=PlayerRepository()


        self.assertEqual(len(r.players),0)
        self.assertEqual(r.count,0)

    def test_add_player(self):
        r=PlayerRepository()
        p=Advanced("R")
        r.add(p)
        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)

    def test_add_existing_player(self):
        r=PlayerRepository()
        p=Advanced("R")
        r.add(p)
        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)
        with self.assertRaises(ValueError):
            r.add(p)
        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)

    def test_remove_existing_player(self):
        r=PlayerRepository()
        p=Advanced("R")
        r.add(p)
        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)

        r.remove(p.username)
        self.assertEqual(len(r.players), 0)
        self.assertEqual(r.count, 0)

    def test_remove_nonexisting_player(self):
        r=PlayerRepository()
        p=Advanced("Test")

        self.assertEqual(len(r.players), 0)
        self.assertEqual(r.count, 0)

        with self.assertRaises(ValueError):
            r.remove("")
        self.assertEqual(len(r.players), 0)
        self.assertEqual(r.count, 0)
    def test_find_player(self):
        r=PlayerRepository()
        p=Advanced("Test")

        r.add(p)

        self.assertEqual(len(r.players), 1)
        self.assertEqual(r.count, 1)


        self.assertEqual(r.find("Test"),p)
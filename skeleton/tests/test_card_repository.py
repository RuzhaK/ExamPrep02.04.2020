import unittest

from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository


class TestRepository(unittest.TestCase):
    def test_init_card_set_attributes(self):
        r=CardRepository()


        self.assertEqual(len(r.cards),0)
        self.assertEqual(r.count,0)

    def test_add_card(self):
        r=CardRepository()
        p=MagicCard("R")
        r.add(p)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

    def test_add_existing_card(self):
        r=CardRepository()
        p=MagicCard("R")
        r.add(p)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)
        with self.assertRaises(ValueError):
            r.add(p)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

    def test_remove_existing_card(self):
        r=CardRepository()
        p=MagicCard("R")
        r.add(p)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

        r.remove(p.name)
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)

    def test_remove_nonexisting_card(self):
        r=CardRepository()
        p=MagicCard("Test")

        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)

        with self.assertRaises(ValueError):
            r.remove("")
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)
    def test_find_card(self):
        r=CardRepository()
        p=MagicCard("Test")

        r.add(p)

        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)


        self.assertEqual(r.find("Test"),p)
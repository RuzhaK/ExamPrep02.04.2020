import unittest

from project.card.trap_card import TrapCard

DAMAGE_POINTS = 120
INITIAL_HEALTH_POINTS = 5


class TestTrapCard(unittest.TestCase):
    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            advanced = TrapCard("")

    def test_name_is_set(self):
        advanced = TrapCard("Test")
        self.assertEqual(advanced.name, "Test")

    def test_health_is_set(self):
        advanced = TrapCard("Test")
        self.assertEqual(advanced.health_points, INITIAL_HEALTH_POINTS)
        self.assertEqual(advanced.damage_points, DAMAGE_POINTS)

    def test_health_negative_value_raises(self):
        advanced = TrapCard("Test")
        with self.assertRaises(ValueError):
            advanced.health_points = -10

    def test_damage_is_set(self):
        advanced = TrapCard("Test")

        self.assertEqual(advanced.damage_points, DAMAGE_POINTS)

    def test_damage_negative_value_raises(self):
        advanced = TrapCard("Test")
        with self.assertRaises(ValueError):
            advanced.damage_points = -10
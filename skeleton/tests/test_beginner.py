from unittest import TestCase

from project.player.beginner import Beginner

INITIAL_HEALTH_POINTS = 50


class TestAdvanced(TestCase):
    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            advanced = Beginner("")

    def test_name_is_set(self):
        advanced = Beginner("Test")
        self.assertEqual(advanced.username, "Test")

    def test_health_is_set(self):
        advanced = Beginner("Test")
        self.assertEqual(advanced.health, INITIAL_HEALTH_POINTS)

    def test_health_negative_value_raises(self):
        advanced = Beginner("Test")
        with self.assertRaises(ValueError):
            advanced.health = -10

    def test_is_dead(self):
        advanced = Beginner("Test")
        self.assertEqual(advanced.health, INITIAL_HEALTH_POINTS)
        self.assertFalse(advanced.is_dead)
        advanced.health = 0
        self.assertEqual(advanced.health, 0)
        self.assertTrue(advanced.is_dead)

    def tet_take_damage_raises_with_negative_value(self):
        advanced = Beginner("Test")
        self.assertEqual(advanced.health, INITIAL_HEALTH_POINTS)
        with self.assertRaises(ValueError):
            advanced.take_damage(-50)

    def tet_take_damage_positive_value(self):
        advanced = Beginner("Test")
        self.assertEqual(advanced.health, INITIAL_HEALTH_POINTS)
        advanced.take_damage(50)
        self.assertEqual(advanced.health, 0)

    def tet_take_damage_positive_value_player_will_be_dead(self):
        advanced = Beginner("Test")
        self.assertEqual(advanced.health, INITIAL_HEALTH_POINTS)
        with self.assertRaises(ValueError):
            advanced.take_damage(260)



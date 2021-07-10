from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository


class Player(ABC):
    @abstractmethod
    def __init__(self,username: str, health:int):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()



    @property
    def is_dead(self):
        return True if self.health<=0 else False





    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._validate_username(value)
        self._username=value


    @staticmethod
    def _validate_username( value):
        if value=="":
            raise ValueError("Player's username cannot be an empty string. ")

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._validate_health(value)
        self._health = value

    def _validate_health(self, value):
        if value <0:
            raise ValueError("Player's health bonus cannot be less than zero. ")


    def take_damage (self,damage_points:int):
        self._validate_damage(damage_points)
        self.health-=damage_points

    @staticmethod
    def _validate_damage(damage_points):
        if damage_points<0:
            raise ValueError( "Damage points cannot be less than zero.")


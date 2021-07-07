from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository


class Player(ABC):
    @abstractmethod
    def __init__(self,username: str, health:int):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()
        self.is_dead:bool=False


    @property
    def is_dead(self):
        return self.__is_dead

    @is_dead.setter
    def is_dead(self, value):
        if self.health>0:
            self.__is_dead =False
        else:
            self.__is_dead=True



    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_expenses(value)
        self.__username=value


    @staticmethod
    def __validate_expenses( value):
        if value=="":
            raise ValueError("Player's username cannot be an empty string. ")

    @property
    def health(self):
        return self.__username

    @health.setter
    def health(self, value):
        self.__validate_health(value)
        self.__health = value

    def __validate_health(self, value):
        if value <0:
            raise ValueError("Player's health bonus cannot be less than zero. ")


    def take_damage (self,damage_points:int):
        self.__validate_damage(damage_points)
        self.health-=damage_points

    @staticmethod
    def __validate_damage(damage_points):
        if damage_points<0:
            raise ValueError( "Damage points cannot be less than zero.")
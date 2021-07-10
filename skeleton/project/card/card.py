from abc import ABC, abstractmethod

class Card(ABC):
    @abstractmethod
    def __init__(self, name:str, damage_points:int, health_points:int):
        self.name = name
        self.damage_points = damage_points
        self.health_points = health_points

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value=="":
            raise ValueError("Card's name cannot be an empty string.")
        self._name = value

    @property
    def damage_points(self):
        return self._damage_points

    @damage_points.setter
    def damage_points(self, value):
        self._validate_damage(value)
        self._damage_points = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        self._validate_health(value)
        self._health_points = value


    def _validate_health(self,value):
        if value < 0:
            raise ValueError("Card's HP cannot be less than zero.")

    def _validate_damage(self, value):
        if value < 0:
            raise ValueError("Card's damage points cannot be less than zero.")

# a=Card("ssd",10,0)
# a.damage_points=-10
from project.card.card import Card

class MagicCard(Card):
    initial_damage_points=5
    initial_health_points=80
    def __init__(self,name):
        super().__init__(name,self.initial_damage_points,self.initial_health_points)

# m=MagicCard("www")
# m.damage_points=-10
# m.health_points=-1
# print(m.damage_points)
a=5
print(a)
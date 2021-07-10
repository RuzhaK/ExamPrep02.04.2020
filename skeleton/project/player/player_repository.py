from project.player.player import Player


class PlayerRepository():
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self,player: Player):
        names=[player.username for player in self.players]
        # names=list(map(lambda x:x.name, self.players))
        if player.username not in names:
            self.players.append(player)
            self.count+=1
        else:
            raise ValueError(f"Player {player.username} already exists!")


    def remove(self,player_name: str):
        if player_name=="":
            raise ValueError("Player cannot be an empty string!")
        else:

            player_object=[p for p in self.players if p.username==player_name][0]
            # player_object=list(filter(lambda x: x.username==player, self.players))[0]
            self.players.remove(player_object)
            self.count-=1


    def find(self,username: str):
        player=[x for x in self.players if x.username==username][0]
        if player:
            return player

# r=PlayerRepository()
# print(r.players)
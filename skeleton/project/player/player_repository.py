from project.player.player import Player


class PlayerRepository():
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self,player: Player):
        if player not in self.players:
            self.players.append(player)
            self.count+=1
        else:
            raise ValueError(f"Player {player.username} already exists!")


    def remove(self,player: str):
        if player=="":
            raise ValueError("Player cannot be an empty string!")
        else:
            if player in self.players:
                self.players.remove(player)
                self.count-=1

    def find(self,username: str):
        player=[x for x in self.players if x.username==username][0]
        if player:
            return player
from Insect import Insect

class Hornet(Insect):
    attack: int

    def __init__(self, tile, health, attack):
        self.tile = tile
        self.health = health
        self.attack = attack

    def takeAction(self):
        if self.tile.getBee() != None:
            self.tile.getBee().takeDamage(self.attack)
        else:
            if self.tile.isHive():
                pass
            else:
                self.tile = self.tile.towardTheHive()
        return True
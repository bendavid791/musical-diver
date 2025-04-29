from HoneyBee import HoneyBee

class AngryBee(HoneyBee):
    attack: int

    def __init__(self, tile, attack):
        self.tile = tile
        self.attack = attack
        self.health = 10
        self.food_cost = 1

    def takeAction(self):
        if not self.tile.isOnThePath():
            return False
        else:
            if self.tile.getHornet() != None:
                self.tile.getHornet().takeDamage(self.attack)
                return True
            else:
                return False
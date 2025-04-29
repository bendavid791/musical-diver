from HoneyBee import HoneyBee

class TankBee(HoneyBee):
    attack: int
    armor: int

    def __init__(self, tile, attack, armor):
        self.tile = tile
        self.attack = attack
        self.armor = armor
        self.health = 30
        self.food_cost = 3

    def takeAction(self):
        if not self.tile.isOnThePath():
            return False
        else:
            if self.tile.getHornet() != None:
                self.tile.getHornet().takeDamage(self.attack)
                return True
            else:
                return False
    
    def takeDamage(self, dmg: int):
        dmg = int(round(dmg*100/(100 + self.armor), 0))
        super().takeDamage(dmg)
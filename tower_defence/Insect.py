class Insect:
    tile: "Tile" # type: ignore
    health: int

    def __init__(self, tile):
        self.tile = tile
        if tile.addInsect(self):
            pass
        else:
            raise ValueError("Cannot add insect to tile. Either there is already a honeybee there, or some other error.")

    def getPosition(self):
        return self.tile

    def getHealth(self):
        return self.health
    
    def setPosition(self, tile):
        self.tile = tile

    def takeDamage(self, dmg):
        if self.tile.beehive_present:
            dmg = int(round(dmg*0.9, 0))
        self.health -= dmg
        if self.health <= 0:
            self.tile.removeInsect(self)
            self.tile = None
            
    def equals(self, obj):
        if isinstance(obj, type(self)) and self.health == obj.getHealth() and self.position == obj.getPosition():
            return True
        else:
            return False
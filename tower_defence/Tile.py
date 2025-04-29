from HoneyBee import HoneyBee
from Hornet import Hornet
from SwarmOfHornets import SwarmOfHornets

class Tile:
    food_present: int
    beehive_present: bool
    hornet_hive_present: bool
    on_path: bool
    next_tile_towards_bees: "Tile"
    next_tile_towards_hornets: "Tile"
    honeybee: "HoneyBee"
    swarmofhornets: "SwarmOfHornets"

    def __init__(
        self,
        food_present: int = 0,
        beehive_present: bool = False,
        hornet_hive_present: bool = False,
        on_path: bool = False,
        next_tile_towards_bees: "Tile" = None,
        next_tile_towards_hornets: "Tile" = None,
        honeybee: "HoneyBee" = None,
        swarmofhornets: "SwarmOfHornets" = None
    ):
        self.food_present = food_present
        self.beehive_present = beehive_present
        self.hornet_hive_present = hornet_hive_present
        self.on_path = on_path
        self.next_tile_towards_bees = next_tile_towards_bees
        self.next_tile_towards_hornets = next_tile_towards_hornets
        self.honeybee = honeybee
        self.swarmofhornets = swarmofhornets

    def isHive(self):
        return self.beehive_present
    
    def isNest(self):
        return self.hornet_hive_present
    
    def buildHive(self):
        self.beehive_present = True
    
    def buildNest(self):
        self.hornet_hive_present = True

    def isOnThePath(self):
        if self.on_path:
            return self.on_path
        else:
            return None
    
    def towardTheHive(self):
        if self.on_path:
            return self.next_tile_towards_bees
        else:
            return None
        
    def createPath(self, tile1, tile2):
        self.on_path = True
        self.next_tile_towards_bees = tile1
        self.next_tile_towards_hornets = tile2

    def collectFood(self):
        food = self.food_present
        self.food_present = 0
        return food
    
    def storeFood(self, food):
        self.food_present += food
    
    def getBee(self):
        return self.honeybee
    
    def getHornet(self):
        if len(self.swarmofhornets)>0:
            return self.swarmofhornets[0]
        else:
            return None
    
    def getNumOfHornets(self):
        if len(self.swarmofhornets)>0:
            return len(self.swarmofhornets[0])
        else:
            return 0
        
    def addInsect(self, insect):
        if isinstance(insect, HoneyBee):
            if isinstance(self.honeybee, HoneyBee) or self.hornet_hive_present:
                return False
            else:
                self.honeybee = insect
                insect.setPosition(self)
                return True
        elif isinstance(insect, Hornet):
            if self.on_path or self.beehive_present or self.hornet_hive_present:
                if isinstance(self.swarmofhornets, SwarmOfHornets):
                    self.swarmofhornets.addHornet(insect)
                    insect.setPosition(self)
                else:
                    self.swarmofhornets = SwarmOfHornets()
                    self.swarmofhornets.addHornet(insect)
                    insect.setPosition(self)
                return True
            else:
                return False
            
    def removeInsect(self, insect):
        if isinstance(insect, HoneyBee):
            insect.setPosition = None
            self.honeybee = None
            return True
        elif isinstance(insect, Hornet):
            insect.setPosition = None
            self.swarmofhornets.removeHornet(insect)
            return True
        else:
            return False
            
        
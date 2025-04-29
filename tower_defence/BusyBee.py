from HoneyBee import HoneyBee
class BusyBee(HoneyBee):

    def __init__(self, tile):
        self.tile = tile
        self.health = 5
        self.food_cost = 2
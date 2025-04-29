from Insect import Insect

class HoneyBee(Insect):
    food_cost: int

    def __init__(self, tile, health, food_cost):
        self.tile = tile
        self.health = health
        self.food_cost = food_cost

    def getCost(self):
        return self.food_cost
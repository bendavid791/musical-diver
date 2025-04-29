from Hornet import Hornet

class SwarmOfHornets:
    hornets: list["Hornet"]
    size: int

    def __init__(self):
        # generates empty list, there are no hornets in the swarm.
        self.hornets = []
        self.size = 0

    def sizeOfSwarm(self):
        return self.size
    
    def getHornets(self):
        return self.hornets
    
    def getFirstHornet(self):
        if self.size > 0:
            return self.hornets[0]
        else:
            return None
        
    def addHornet(self, hornet):
        self.hornets.append(hornet)
        self.size += 1

    def removeHornet(self, target: "Hornet"):
        # remove the first occurence of the specified hornet in the swarm.
        if self.size > 0:
            for i, hornet in enumerate(self.hornets):
                if hornet is target:
                    del self.hornets[i]
                    self.size -= 1
                    return True
            return False
        else:
            return False
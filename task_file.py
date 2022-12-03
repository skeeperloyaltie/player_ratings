# %%
class PlayerTransfer:
    def __init__(self, speed, shooting, passing, defending, dribbling, physicality):
        self.speed = speed
        self.shooting = shooting
        self.passing = passing
        self.defending = defending
        self.dribbling = dribbling
        self.physicality = physicality
    # setters
    def setSpeed(self, speed):
        self.speed = speed

    def setShooting(self, shooting):
        self.shooting = shooting

    def setPassing(self, passing):
        self.passing = passing

    def setDefending(self, defending):
        self.defending = defending

    def setDribbling(self, dribbling):
        self.dribbling = dribbling

    def setPhysicality(self, physicality):
        self.physicality = physicality
    # getters
    def getSpeed(self):
        return self.speed

    def getShooting(self):
        return self.shooting

    def getPassing(self):
        return self.passing

    def getDefending(self):
        return self.defending

    def getDribbling(self):
        return self.dribbling

    def getPhysicality(self):
        return self.physicality

    # functions to calculate salary
    def calculateoveral_rate(self):
        total_skills = self.speed + self.shooting + self.physicality + self.dribbling + self.defending + self.passing
        overal_rate = total_skills * (100/30)
        
        if overal_rate > 29 and overal_rate < 45:
            salary = 400
            return overal_rate, salary
        elif overal_rate > 44 and overal_rate < 60:
            salary = [500, 700]
            return overal_rate, salary
        elif overal_rate > 59 and overal_rate < 80:
            salary = 700
            return overal_rate, salary
        elif overal_rate > 79 < 101:
            salary = 1000
            return overal_rate, salary
        

# %%
def main():
    speed = int(input('Enter Speed of Player: '))
    dribbling = int(input('Enter Dribbling of Player: '))
    passing = int(input('Enter passing of player: '))
    shooting = int(input('Enter shooting of player: '))
    defending = int(input('Enter defending of player: '))
    physicality = int(input('Enter physicality of player: '))
    player = PlayerTransfer(speed, dribbling, passing, shooting, defending, physicality)
    player.setDefending(defending)
    player.setDribbling(dribbling)
    player.setPassing(passing)
    player.setPhysicality(physicality)
    player.setShooting(shooting)
    player.setSpeed(speed)
    player.getDefending()
    player.getDribbling()
    player.getPassing()
    player.getPhysicality()
    player.getSpeed()
    player.getShooting()

    print('Player stats\nSpeed: {}\nPhysicality: {}\nShooting: {}\nDribbling: {}\nDefending: {}\nPassing: {}\nRating: {}\n'.format(speed, physicality, shooting, dribbling, defending, passing, player.calculateoveral_rate()))

if __name__ == '__main__':
    main()



class Enemy(object):
    def fight(self):
        pass

class Thug(Enemy):
    def __init__(self):
        self.health = 30

class Boss(Enemy):

    def __init__(self):
    self.health = 100

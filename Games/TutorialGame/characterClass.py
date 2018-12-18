class Character(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.attacks = 8
        self.armor = 100

    def __str__(self):
        if self.alive:
            return "%s(%i armor, %i attacks)" %(self.name, self.armor, self.attacks)
        else:
            return "%s(is kill)" %self.name

    def fire_at(self,enemy):
        if self.attacks>=1:
            self.attacks-=1
            print (self.name, "attacks", enemy.name)
            enemy.hit()
        else:
            print (self.name, "has no more attacks")

    def hit(self):
        self.armor -=20
        print (self.name, "is hit")
        if self.armor<=0:
            self.die()

    def die(self):
        self.alive = False
        print (self.name, "is kill")

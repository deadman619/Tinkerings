import random

class Player(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.damage = random.randint(10,20)
        self.hp = 50

    def __str__(self):
        if self.alive:
            return '%s(Status: Health %i, Damage %i)' %(self.name, self.hp, self.damage)
        else:
            return "('%s dies')" %self.name

    def atk(self, enemy):
        crit = random.randint(0,10)
        if crit == 0:
            print (self.name, "CRITICALLY attacks", enemy.name, "for %i damage" %(self.damage * 2))
            enemy.hp -= self.damage * 2
        elif crit >= 1:
            print (self.name, "attacks", enemy.name, "for %i damage" %self.damage)
            enemy.hp -= self.damage
        enemy.lifecheck()

    def heal(self):
        healamount = random.randint(15,25)
        self.hp += healamount
        print (self.name, "healed for", healamount)
    
    def hit(enemy):
        enemy.hp -= self.damage

    def lifecheck(self):
        if self.hp <=0:
            self.die()

    def die(self):
        self.alive = False

class Alien(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.damage = random.randint(5,15)
        self.hp= random.randint (25, 40)

    def __str__(self):
        if self.alive:
            return '%s(Status: Health %i, Damage %i)' %(self.name, self.hp, self.damage)
        else:
            return "('%s dies')" %self.name

    def atk(self, enemy):
        print (self.name, "attacks", enemy.name, "for %i damage" %self.damage)
        enemy.hp-=self.damage
        enemy.lifecheck()
        
    def weakened_atk(self, enemy):
        lesserDamage = self.damage - 5
        print (self.name, "attacks", enemy.name, "for %i damage. Your defense lessened the damage." %lesserDamage)
        enemy.hp-=lesserDamage

    def hit(enemy):
        enemy.hp -= self.damage

    def lifecheck(self):
        if self.hp <=0:
            self.die()

    def die(self):
        self.alive = False
    

from random import randint


class Pykatchu:
    def __init__(self,name,noise, health, strength, armor, bonus):
        self.name = name
        self.noise = noise
        self.health = health
        self.strength = strength
        self.armor = armor
        self.bonus = bonus

    def getName(self):
        return self.name

    def getAttackNoise(self):
        return self.noise

    def attack(self, other):
        attacker = self.bonus + self.strength
        print (self.name + " hits " + str(attacker))
        defender = other.bonus + other.armor
        print (other.name + "defends " + str(defender))
        delta = attacker - defender

        print ("")
        if (attacker) > (defender) and delta > 0:
            other.health = other.health - (delta)
            print (self.name + " health: " + str(self.health))
            print (other.name + " health: " + str(other.health))
            return True
        else:
            return False


    def isDead(self):
        if self.health <= 0:
            return True
        else:
            return False


class Pikatchu(Pykatchu):
    def __init__ (self):
        Pykatchu.__init__(self, "Pikatchu:","Pikaaaaaaaaa", randint(1,6), randint(1,6), randint(1,6), randint(1,4))


class Aipom(Pykatchu):
    def __init__ (self):
        Pykatchu.__init__(self, "Aipom: ","Aipoooooom", randint(1,6), randint(1,6), randint(1,6), randint(1,4))



#   Falls into a loop of every x amount of server restarts.
#
#
# class Pikatchu(Pykatchu):
#     def __init__ (self):
#         Pykatchu.__init__(self, "Pikatchu:","Pikaaaaaaaaa", randint(1,6), randint(1,6), randint(1,6), randint(1,4))
#
#
# class Aipom(Pykatchu):
#     def __init__ (self):
#         Pykatchu.__init__(self, "Aipom: ","Aipoooooom", randint(1,6), randint(1,6), randint(1,6), randint(1,4))

# Soldier
import unittest
from vikingsClasses import Soldier
form inspect import signature


class Soldier:
    def_init_(self,health, strength):
        self.health = health
        self.strength = strength
        

    pass

# Viking


class Viking:
    def_init_(self, name, health, strength):
        self.name = name
        super()._init_(health, strength)
 
    def receiveDamage/self, damage):
        self.health -= damage

        if self.health > 0:
            return f"{self.name} has received {str(damage)} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"



# Saxon


class Saxon:
    class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        dmg = saxon.receiveDamage(viking.strength)

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)

        return dmg

    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        
        dmg = viking.receiveDamage(saxon.strength)

        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        
        return dmg

    def showStatus(self):
        if not self.saxonArmy:
            return f"Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."

import os
os.system('cls')

from names import list_names
from random import randint, random
import random

class Actor:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
        

    def __repr__(self):
        return '<Actor: {}, Level:{}'.format(self.name, self.level)

    def get_attack_power(self): 
        return randint(1,20) * self.level
    
    def is_alive(self):
        return self.health > 0
    
    def health(self):
        return self.health * self.level
    
    def attacks(self, other):
        raise NotImplementedError()
    

class Player(Actor):
    def __init__(self, name, level, health):
        super().__init__(name, level, health)
        self.xp = 0
        self.xp_to_next_level = 100

    def gain_xp(self, amount):
        self.xp += amount
        print(f'{self.name} gained {amount} XP! Total XP: {self.xp}')
        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level_up()
            self.xp_to_next_level = int(self.xp_to_next_level * 1.5) #increases the amount of xp needed for the next level 
            
    def heal(self):
        self.health = self.health + 10
    
    
    def attacks(self, enemy):
        power = self.get_attack_power()
        
        print('{} attacks the {}'.format(self.name, enemy.kind))
        print('{} did {} attack damage'.format(self.name, power))
        enemy.health -= power

    def level_up(self):
        self.level += 1

        print('{} leveled up! You are now level {}'.format(self.name, self.level))

    def stats(self):
        print('{} has {} hp, is level {}, and has {}/{} XP'.format(self.name, self.health, self.level, self.xp, self.xp_to_next_level))

class Enemy(Actor):
    def __init__(self, kind, level, health, name=None):
        if name is None:
            name = random.choice(list_names)
        super().__init__(name, level, health)
        self.kind = kind
    def attacks(self, player):
        print('{} the {} attacks {}'.format(self.name, self.kind, player.name))
        e_power = self.get_attack_power()
        print('{} attacks you with {} attack damage'.format(self.name, e_power))
        player.health -= e_power

    def stats(self):
        print(f'{self.name} the {self.kind} has {self.health} hp, and is level {self.level}'.format(self.name, self.kind, self.health, self.level))

class Ogre(Enemy):
    def __init__(self, health, level, size, name):
        super().__init__('Ogre', level, health, name)
        self.size = size 
    
    def get_attack_power(self):
        return randint(1,50) * (self.size * self.level)
    
class Goblin(Enemy):
    def __init__(self, level, health, name, weapon):
        super().__init__('Goblin', level, health, name)
        self.weapon = weapon

    def get_attack_power(self):
        return randint(1,25) * (self.weapon * self.level)

class Imp(Enemy):
    def __init__(self, level, health, name):
        super().__init__('Imp', level, health, name)

    def get_attack_power(self):
        return super().get_attack_power() / 4
    
        
if __name__ == '__main__':
    player = Player(name='Luffy', level=1, health=100)
    
    
    
        
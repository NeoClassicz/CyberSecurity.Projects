import os
os.system('cls')

from random import randint

class Actor:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def __repr__(self):
        return '<Actor: {}, Level:{}'.format(self.name, self.level)

    def get_attack_power(self): 
        return randint(1,100) * self.level
    
    def is_alive(self):
        return self.health > 0
    
    def health(self):
        return self.health * self.level
    
    def attacks(self, other):
        raise NotImplementedError()
    
    def stats(self):
        print('{} has {} hp'.format(self.name, self.health))

class Player(Actor):
    def heal(self):
        self.health = self.health + 10
    
    def attacks(self, enemy):
        power = self.get_attack_power()
        
        print('{} attacks the {}'.format(self.name, enemy.kind))
        print('{} has {} attack power'.format(self.name, power))
        enemy.health -= power

class Enemy(Actor):
    def __init__(self, kind, level, health, name):
        super().__init__(name, level, health)
        self.kind = kind
    
    def attacks(self, player):
        print('{} the {} attacks {}'.format(self.name, self.kind, player.name))
        e_power = self.get_attack_power()
        print('{} has {} attack power'.format(self.name, e_power))
        player.health -= e_power
    
class Ogre(Enemy):
    def __init__(self, health, name, level, size):
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
    player = Player(name='Luffy', level=1, health=1000)
    
    
    
        
from random import randint
import random  # Add this import
from Learning.Text_based_game.names import list_names
import os
os.system('cls')

# You can also add `randint` here specifically if you want:


class Actor:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def __repr__(self):
        return '<Actor: {}, Level:{}'.format(self.name, self.level)

    def get_attack_power(self):
        # Now works because randint is imported
        return randint(1, 20) * self.level

    def is_alive(self):
        return self.health > 0

    def max_health(self):  # Renamed to avoid conflict with the health attribute
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
            self.xp_to_next_level = int(self.xp_to_next_level * 1.5)

    def heal(self):
        self.health += 10

    def attacks(self, enemy):
        power = self.get_attack_power()
        print(f'{self.name} attacks {enemy.name} the {enemy.kind}')
        print(f'{self.name} did {power} attack damage')
        enemy.health -= power

    def level_up(self):
        self.level += 1
        print(f'{self.name} leveled up! You are now level {self.level}')

    def stats(self):
        print(f'{self.name} has {self.health} hp, is level {self.level}, and has {self.xp}/{self.xp_to_next_level} XP')


class Enemy(Actor):
    def __init__(self, kind, level, health, size=None, weapon=None, name=None):
        if name is None:
            name = random.choice(list_names)
        super().__init__(name, level, health)
        self.kind = kind
        self.size = size
        self.weapon = weapon

    def attacks(self, player):
        print(f'{self.name} the {self.kind} attacks {player.name}')
        e_power = self.get_attack_power()
        print(f'{self.name} attacks you with {e_power} attack damage')
        player.health -= e_power

    def stats(self):
        size_str = None
        if self.size is not None:
            if isinstance(self.size, int):
                size_map = {1: 'small', 2: 'medium', 3: 'large'}
                size_str = size_map.get(self.size, str(self.size))
            else:
                size_str = str(self.size)

        if size_str:
            print(
                f'{self.name} the {size_str} {self.kind} has {self.health} hp, and is level {self.level}')
        elif self.weapon is not None:
            print(
                f'{self.name} the {self.kind} (Weapon: {self.weapon}) has {self.health} hp, and is level {self.level}')
        else:
            print(
                f'{self.name} the {self.kind} has {self.health} hp, and is level {self.level}')


class Ogre(Enemy):
    def __init__(self, health, level, size, name=None):
        super().__init__('Ogre', level, health, size=size, name=name)

    def get_attack_power(self):
        return randint(1, 50) * (self.size * self.level)


class Goblin(Enemy):
    def __init__(self, level, health, weapon, name=None):
        super().__init__('Goblin', level, health, weapon=weapon, name=name)

    def get_attack_power(self):
        return randint(1, 25) * (self.weapon * self.level)


class Imp(Enemy):
    def __init__(self, level, health, name=None):
        super().__init__('Imp', level, health, name=name)

    def get_attack_power(self):
        return super().get_attack_power() // 4  # Imp has weaker attack power


if __name__ == '__main__':
    player = Player(name='Luffy', level=1, health=100)

from Learning.Text_based_game.characters import Player, Enemy, Ogre, Goblin, Imp
import random
from random import randint
import os
os.system('cls')


class Game:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies
        self.player.has_healed = False
        self.current_enemy = None

    def main(self):
        self.print_intro()
        self.play()

    def print_intro(self):
        print(''' 
                Welcome to Level Up! 
                Ready to fight your way to victory?
                [Press Enter to Continue] 
                ''')
        input()

    def print_linebreak(self):
        print()
        print('-'*30)
        print()

    def play(self):
        while True:
            if self.current_enemy is None:  # There is no current enemy so it picks a new one.
                self.current_enemy = random.choice(self.enemies)

            cmd = input(
                f'You see {self.current_enemy.name} the {self.current_enemy.kind}. [r]un, [a]ttack, [h]eal, [p]ass? ')
            os.system('cls')

            if cmd.lower() == 'r':
                print(f'{self.player.name} runs away!')
                # Reset the current enemy after running away.
                self.current_enemy = None

            elif cmd.lower() == 'h':
                if not self.player.has_healed:
                    print(f"{self.player.name} heals themselve's!")
                    self.player.heal()
                    self.player.has_healed = True
                else:
                    print(f"{self.player.name} has already healed!")

            elif cmd.lower() == 'a':
                self.player.attacks(self.current_enemy)
                if not self.current_enemy.is_alive():
                    self.enemies.remove(self.current_enemy)
                    xp_earned = self.current_enemy.level * 50  # Calculate XP earned
                    self.player.gain_xp(xp_earned)
                    print(
                        f'{self.player.name} has slayed the {self.current_enemy.kind}!')
                    self.current_enemy = None  # Reset current enemy
                if self.current_enemy and self.current_enemy.is_alive():
                    self.current_enemy.attacks(self.player)

            elif cmd.lower() == 'p':
                print('You are still thinking about your next move...')
                if random.randint(1, 11) < 5:
                    self.current_enemy.attacks(self.player)

            else:
                print('Please choose a valid option')

            if not self.player.is_alive():
                print('OH NO! You lose...')
                break

            self.print_linebreak()
            self.player.stats()
            self.print_linebreak()
            for e in self.enemies:
                e.stats()
            self.print_linebreak()

            if not self.enemies:
                print('You have won! Congratulations.')
                break


if __name__ == '__main__':
    player = Player('Luffy', 1, health=50)
    enemies = [
        Ogre(health=40, level=1, size=1),
        Ogre(health=40, level=1, size=random.randint(1, 3)),
        Goblin(level=1, health=20, weapon=1),
        Imp(level=1, health=10),
    ]

    game = Game(player, enemies)
    game.main()

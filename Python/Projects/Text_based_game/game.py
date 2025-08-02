import random
import os 
os.system('cls')
from characters import Player, Enemy, Ogre, Goblin, Imp

class Game:
        def __init__(self, player, enemies):
            self.player = player
            self.enemies = enemies
        
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
                next_enemy = random.choice(self.enemies)
                cmd = input('You see an {}. [r]un, [a]ttack, [p]ass? '.format(next_enemy.kind))
                if cmd.lower() == 'r':
                    print('{} runs away! '.format(self.player.name))
                    print("{} heals themselve's!".format(self.player.name))
                    self.player.heal()

                elif cmd.lower() == "a": 
                    print('{} attacks the {}'.format(self.player.name, next_enemy.kind))
                    self.player.attacks(next_enemy)
                    if not next_enemy.is_alive():
                        self.enemies.remove(next_enemy)
                    next_enemy.attacks(self.player)
                    if not self.player.is_alive():
                        print('OH NO! You lose...')
                        break

                elif cmd.lower()== 'p':
                    print('You are still thinking about your next move...')
                    if random.randint(1,11) < 5:
                        next_enemy.attacks(self.player)

                else:
                    print('Please choose a valid option')

                self.print_linebreak()
                self.player.stats()
                for e in self.enemies:
                    e.stats()
                self.print_linebreak()

                if not self.enemies:
                    print('You have won! Congratulations.')
                    break
        
if __name__ == '__main__': #this code only runs if this file is being run directly so game.py

    enemies = [
        Ogre(name='Jon', level=1, health=40, size=1),
        Goblin(name='bob', level=1, health=20, weapon=1),
        Imp(name='little guy', level=1, health=10)
    ]
    player = Player('Luffy', 1, health=100)
    
    game = Game(player, enemies).main()

import random
import os 
os.system('cls')
from characters import Player, Enemy, Ogre, Goblin, Imp

class Game:
        def __init__(self, player, enemies):
            self.player = player
            self.enemies = enemies
            self.player.has_healed = False

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
                cmd = input('You see an {}. [r]un, [a]ttack, [h]eal, [p]ass? '.format(next_enemy.kind))
                os.system('cls')
                if cmd.lower() == 'r':
                    print('{} runs away! '.format(self.player.name))
            

                elif cmd.lower() == 'h':
                    if not self.player.has_healed:
                        print("{} heals themselve's!".format(self.player.name))
                        self.player.heal()
                        self.player.has_healed = True
                    else:
                        print("{} has already healed!".format(self.player.name))

                elif cmd.lower() == "a": 
                    self.player.attacks(next_enemy)
                    if not next_enemy.is_alive():
                        self.enemies.remove(next_enemy)
                        self.player.has_healed = False
                        print('{} has slayed the {}!'.format(player.name, next_enemy.kind))
                        xp_earned = next_enemy.level * 50
                        self.player.gain_xp(xp_earned)
                        next_enemy = None
                    if next_enemy:   
                        next_enemy.attacks(self.player)

                elif cmd.lower()== 'p':
                    print('You are still thinking about your next move...')
                    if random.randint(1,11) < 5:
                        next_enemy.attacks(self.player)

                else:
                    print('Please choose a valid option')

                if not self.player.is_alive():
                        print('OH NO! You lose...')
                        break
            
                self.print_linebreak()
                self.player.stats()
                for e in self.enemies:
                    e.stats()
                self.print_linebreak()

                if not self.enemies:
                    print('You have won! Congratulations.')
                    break
                
                
        
if __name__ == '__main__': #this code only runs if this file is being run directly so game.py
    
    player = Player('Luffy', 1, health=50)
    enemies = [
        Ogre(name=None,level=1, health=40, size=1),
        Goblin(name=None, level=1, health=20, weapon=1),
        Imp(name=None,level=1, health=10),
    ]
    
    
    game = Game(player, enemies).main()

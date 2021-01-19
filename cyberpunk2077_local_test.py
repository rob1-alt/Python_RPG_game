import random

baseball_bat = random.randint(6, 11)
knife = random.randint(12, 18)
longsword = random.randint(17, 22)
Axe = random.randint(19, 25)
Katana = random.randint(20, 28)

class Player:
    def __init__(self):
        self.name = ''
        self.max_health = 30
        self.health = self.maxhealth
        self.base_attack = 11
        self.current_attack = 11
        self.weapon = ''
        self.current_weapon = ''

class Maraudeur:
    def __init__(self, name):
        self.name = name
        self.max_health = 12
        self.health = self.maxhealth
        self.attack = baseball_bat

class Miniboss:
    def __init__(self, name):
        self.name = name
        self.max_health = 26
        self.health = self.maxhealth
        self.attack = Axe

class Boss:
    def __init__(self, name):
        self.name = name
        self.max_health = 40
        self.health = self.maxhealth
        self.attack = Katana

def room_one():

def attack():
    print('Que veux tu faire ?')
    option = input("> ")
    if option == "Attaquer":
        enemy.health -= Player.current_attack
    else:
        print('Mauvaise commande')

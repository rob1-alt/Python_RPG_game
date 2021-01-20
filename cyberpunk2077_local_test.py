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
        self.health = self.max_health
        self.base_attack = 11
        self.current_attack = 11
        self.weapon = ''
        self.current_weapon = ''
    def attack(self, enemy):
        enemy.health -= self.current_attack
    def death(self,):
        print('You died')
        print('RIP')
    def win_room(self):
        self.health = 30
        print('you won this room')



class Enemy:
    def __init__(self, name, maxhealth, attack):
        self.name = name
        self.max_health = maxhealth
        self.health = maxhealth
        self.attack = attack
    def attack_enemy(self, player):
        player.health -= self.attack

def room_one():
    print('Tu arrives dans la première salle. Il y a un enemie faible')
    enemy_one = Enemy('Maraudeur', 12, baseball_bat)
    player = Player()
    print("L'enmie a", enemy_one.health, "hp; Tu as", player.health, "hp")
    print('Que veux tu faire ?')
    while (player.health > 1 or enemy_one.health > 1):
        option = input("> ")
        if option == "Attaquer":
            player.attack(enemy_one)
            print('Tu as infligé', player.current_attack, "points de dégats")
            print("L'ennemie a", enemy_one.health, "HP")
            if (enemy_one.health <= 0):
                player.win_room()
                break
            enemy_one.attack_enemy(player)
            print("L'enemie t'as infligé", enemy_one.attack, "points de dégats")
            print('Tu as', player.health, "HP")
            if (player.health <= 0):
                player.death()
        else:
            print('Mauvaise commande')
    print('Veux tu aller à gauche ou à droite ?')
    option = input("> ")
    if (option == 'Gauche'):
        shortcut_room()
    elif (option == 'Droite'):
        street_room()
    else:
        print('Mauvaise Commande')



def shortcut_room():
    print('Gauche')

def street_room():
    print('Droite')

room_one()
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
    while (1):
        option = input("> ")
        if (option == 'Gauche'):
            shortcut_room()
            break
        elif (option == 'Droite'):
            street_room()
            break
        else:
            print('Mauvaise Commande')



def shortcut_room():
    print('Tu arrives dans la deuxième salle. Il y a un enemie moyen')
    enemy_street = Enemy('Maraudeur', 16, knife)
    player = Player()
    print("L'enmie a", enemy_street.health, "hp; Tu as", player.health, "hp")
    print('Que veux tu faire ?')
    while (player.health > 1 or enemy_street.health > 1):
        option = input("> ")
        if option == "Attaquer":
            player.attack(enemy_street)
            print('Tu as infligé', player.current_attack, "points de dégats")
            print("L'ennemie a", enemy_street.health, "HP")
            if (enemy_street.health <= 0):
                player.win_room()
                break
            enemy_street.attack_enemy(player)
            print("L'enemie t'as infligé", enemy_street.attack, "points de dégats")
            print('Tu as', player.health, "HP")
            if (player.health <= 0):
                player.death()
        else:
            print('Mauvaise commande')
    print('Veux tu aller à gauche ou à droite ?')
    while (1):
        option = input("> ")
        if (option == 'Gauche'):
            trapped_room()
            break
        elif (option == 'Droite'):
            miniboss_room()
            break
        else:
            print('Mauvaise Commande')

def street_room():
    print('Tu arrives dans la deuxième salle. Il y a un enemie moyen')
    enemy_street = Enemy('Maraudeur', 16, knife)
    player = Player()
    print("L'enmie a", enemy_street.health, "hp; Tu as", player.health, "hp")
    print('Que veux tu faire ?')
    while (player.health > 1 or enemy_street.health > 1):
        option = input("> ")
        if option == "Attaquer":
            player.attack(enemy_street)
            print('Tu as infligé', player.current_attack, "points de dégats")
            print("L'ennemie a", enemy_street.health, "HP")
            if (enemy_street.health <= 0):
                player.win_room()
                break
            enemy_street.attack_enemy(player)
            print("L'enemie t'as infligé", enemy_street.attack, "points de dégats")
            print('Tu as', player.health, "HP")
            if (player.health <= 0):
                player.death()
        else:
            print('Mauvaise commande')
    print('Veux tu aller à gauche ou à droite ?')
    while (1):
        option = input("> ")
        if (option == 'Gauche'):
            miniboss_room()
            break
        elif (option == 'Droite'):
            trapped_room()
            break
        else:
            print('Mauvaise Commande')

def miniboss_room():
    print('Tu arrives dans la troisième salle. Il y a un miniboss')
    enemy_street = Enemy('Royce', 26, Axe)
    player = Player()
    print("L'enmie a", enemy_street.health, "hp; Tu as", player.health, "hp")
    print('Que veux tu faire ?')
    while (player.health > 1 or enemy_street.health > 1):
        option = input("> ")
        if option == "Attaquer":
            player.attack(enemy_street)
            print('Tu as infligé', player.current_attack, "points de dégats")
            print("L'ennemie a", enemy_street.health, "HP")
            if (enemy_street.health <= 0):
                player.win_room()
                break
            enemy_street.attack_enemy(player)
            print("L'enemie t'as infligé", enemy_street.attack, "points de dégats")
            print('Tu as', player.health, "HP")
            if (player.health <= 0):
                player.death()
        else:
            print('Mauvaise commande')
    print('Veux tu aller à gauche ou à droite ?')
    while (1):
        option = input("> ")
        if (option == 'Gauche'):
            ground_floor_room()
            break
        elif (option == 'Droite'):
            basement_room()
            break
        else:
            print('Mauvaise Commande')

def ground_floor_room():
    print('Tu arrives dans la quatrième salle. Il y a un maraudeur normal')
    enemy_street = Enemy('Maraudeur', 16, knife)
    player = Player()
    print("L'enmie a", enemy_street.health, "hp; Tu as", player.health, "hp")
    print('Que veux tu faire ?')
    while (player.health > 1 or enemy_street.health > 1):
        option = input("> ")
        if option == "Attaquer":
            player.attack(enemy_street)
            print('Tu as infligé', player.current_attack, "points de dégats")
            print("L'ennemie a", enemy_street.health, "HP")
            if (enemy_street.health <= 0):
                player.win_room()
                break
            enemy_street.attack_enemy(player)
            print("L'enemie t'as infligé", enemy_street.attack, "points de dégats")
            print('Tu as', player.health, "HP")
            if (player.health <= 0):
                player.death()
        else:
            print('Mauvaise commande')
    print('Veux tu aller à gauche ou à droite ?')
    while (1):
        option = input("> ")
        if (option == 'Gauche'):
            first_floor_light()
            break
        elif (option == 'Droite'):
            first_floor_heavy()
            break
        else:
            print('Mauvaise Commande')

def basement_room():
    print('Tu arrives dans la quatrième salle. Il y a un maraudeur lourd')
    enemy_street = Enemy('Maraudeur', 19, longsword)
    player = Player()
    print("L'enmie a", enemy_street.health, "hp; Tu as", player.health, "hp")
    print('Que veux tu faire ?')
    while (player.health > 1 or enemy_street.health > 1):
        option = input("> ")
        if option == "Attaquer":
            player.attack(enemy_street)
            print('Tu as infligé', player.current_attack, "points de dégats")
            print("L'ennemie a", enemy_street.health, "HP")
            if (enemy_street.health <= 0):
                player.win_room()
                break
            enemy_street.attack_enemy(player)
            print("L'enemie t'as infligé", enemy_street.attack, "points de dégats")
            print('Tu as', player.health, "HP")
            if (player.health <= 0):
                player.death()
        else:
            print('Mauvaise commande')
    print('Veux tu aller à gauche ou à droite ?')
    while (1):
        option = input("> ")
        if (option == 'Gauche'):
            first_floor()
            break
        elif (option == 'Droite'):
            trapped_room()
            break
        else:
            print('Mauvaise Commande')

def first_floor():
    print('Tu arrives dans la cinquième salle. Il y a un maraudeur normal')
    enemy_street = Enemy('Maraudeur', 16, knife)
    player = Player()
    print("L'enmie a", enemy_street.health, "hp; Tu as", player.health, "hp")
    print('Que veux tu faire ?')
    while (player.health > 1 or enemy_street.health > 1):
        option = input("> ")
        if option == "Attaquer":
            player.attack(enemy_street)
            print('Tu as infligé', player.current_attack, "points de dégats")
            print("L'ennemie a", enemy_street.health, "HP")
            if (enemy_street.health <= 0):
                player.win_room()
                break
            enemy_street.attack_enemy(player)
            print("L'enemie t'as infligé", enemy_street.attack, "points de dégats")
            print('Tu as', player.health, "HP")
            if (player.health <= 0):
                player.death()
        else:
            print('Mauvaise commande')
    print('Tu vas rentrer dans la salle du boss')
    boss_room()


def first_floor_light():
    print('Tu arrives dans la cinquième salle. Il y a un maraudeur faible')
    enemy_street = Enemy('Maraudeur', 12, baseball_bat)
    player = Player()
    print("L'enmie a", enemy_street.health, "hp; Tu as", player.health, "hp")
    print('Que veux tu faire ?')
    while (player.health > 1 or enemy_street.health > 1):
        option = input("> ")
        if option == "Attaquer":
            player.attack(enemy_street)
            print('Tu as infligé', player.current_attack, "points de dégats")
            print("L'ennemie a", enemy_street.health, "HP")
            if (enemy_street.health <= 0):
                player.win_room()
                break
            enemy_street.attack_enemy(player)
            print("L'enemie t'as infligé", enemy_street.attack, "points de dégats")
            print('Tu as', player.health, "HP")
            if (player.health <= 0):
                player.death()
        else:
            print('Mauvaise commande')
    print('Tu vas rentrer dans la salle du boss')
    boss_room()

def first_floor_heavy():
    print('Tu arrives dans la cinquième salle. Il y a un maraudeur lourd')
    enemy_street = Enemy('Maraudeur', 19, longsword)
    player = Player()
    print("L'enmie a", enemy_street.health, "hp; Tu as", player.health, "hp")
    print('Que veux tu faire ?')
    while (player.health > 1 or enemy_street.health > 1):
        option = input("> ")
        if option == "Attaquer":
            player.attack(enemy_street)
            print('Tu as infligé', player.current_attack, "points de dégats")
            print("L'ennemie a", enemy_street.health, "HP")
            if (enemy_street.health <= 0):
                player.win_room()
                break
            enemy_street.attack_enemy(player)
            print("L'enemie t'as infligé", enemy_street.attack, "points de dégats")
            print('Tu as', player.health, "HP")
            if (player.health <= 0):
                player.death()
        else:
            print('Mauvaise commande')
    print('Tu vas rentrer dans la salle du boss')
    boss_room()

def boss_room():
    print('Tu arrives dans la sixième salle. Il y a un maraudeur lourd')
    enemy_street = Enemy('Maraudeur', 19, longsword)
    player = Player()
    print("L'enmie a", enemy_street.health, "hp; Tu as", player.health, "hp")
    print('Que veux tu faire ?')
    while (player.health > 1 or enemy_street.health > 1):
        option = input("> ")
        if option == "Attaquer":
            player.attack(enemy_street)
            print('Tu as infligé', player.current_attack, "points de dégats")
            print("L'ennemie a", enemy_street.health, "HP")
            if (enemy_street.health <= 0):
                player.win_room()
                break
            enemy_street.attack_enemy(player)
            print("L'enemie t'as infligé", enemy_street.attack, "points de dégats")
            print('Tu as', player.health, "HP")
            if (player.health <= 0):
                player.death()
        else:
            print('Mauvaise commande')
    print('Veux tu vas rentrer dans la salle du boss')
    print('Tu as gagner, gg')
    input("> ")

def trapped_room():
    Player().death()

room_one()
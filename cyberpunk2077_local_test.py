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
        self.exp = 10
    def attack(self, enemy):
        random_attack = random.randint(1, 8)
        if (random_attack == 1):
            print("tu as manqué ton coup !")
        else:
            enemy.health -= self.current_attack
            print('Bisous')
            print(enemy.health)
    def death(self,):
        print('You died')
        print('RIP')
    def win_room(self):
        self.health = 30
        self.exp += random.randint(24, 38)
        print('you won this room')



class Enemy:
    def __init__(self, name, maxhealth, attack):
        self.name = name
        self.max_health = maxhealth
        self.health = maxhealth
        self.attack = attack
    def attack_enemy(self, player):
        random_enemy_attack = random.randint(1, 6)
        if (random_enemy_attack == 1):
            print("L'enmie à manqué son coup !")
        else:
            player.health -= self.attack

class Room:
    def __init__(self, enemy_one):
        self.enemy = enemy_one

class Jeu:
    def __init__(self, player_one):
        self.room = None
        self.player = player_one
        self.generate_room()
    def generate_room(self):
        player_exp = self.player.exp
        if (player_exp >= 0 & player_exp < 100):
            enemy_weak = Enemy('Maraudeur', 12, baseball_bat)
            self.room = Room(enemy_weak)

def main():
    game = Jeu(Player())
    while (game.player.health > 0):
        while(game.room.enemy.health > 0):
            game.player.attack(game.room.enemy)
            game.room.enemy.attack_enemy(game.player)
        game.player.win_room()
        game.generate_room()
    print("Git Gud")



main()






























# def room_one():
#     room('enemy_one', 'Maraudeur', 12, baseball_bat, 'première', 'faible')
#     print('Veux tu aller à gauche ou à droite ?')
#     two_choice(shortcut_room, street_room)
#
# def shortcut_room():
#     room('shortcut_enemy', 'Maraudeur', 16, knife, 'Deuxième', 'normal')
#     print('Veux tu aller à gauche ou à droite ?')
#     two_choice(trapped_room, miniboss_room)
#
# def street_room():
#     room('enemy_street', 'Maraudeur', 16, knife, 'Deuxième', 'normal')
#     print('Veux tu aller à gauche ou à droite ?')
#     two_choice(miniboss_room, trapped_room)
#
# def miniboss_room():
#     room('miniboss_enemy', 'Royce', 26, Axe, 'Troisième', 'fort')
#     print('Veux tu aller à gauche ou à droite ?')
#     two_choice(ground_floor_room, basement_room)
#
# def ground_floor_room():
#     room('grnd_flr_enemy', 'Maraudeur', 16, knife, 'quatrième', 'normal')
#     print('Veux tu aller à gauche ou à droite ?')
#     two_choice(first_floor_light, first_floor_heavy)
#
# def basement_room():
#     room('basement_enemy', 'Maraudeur', 19, longsword, 'quatrième', 'lourd')
#     print('Veux tu aller à gauche ou à droite ?')
#     two_choice(first_floor, trapped_room)
#
# def first_floor():
#     room('first_floor', 'Maraudeur', 16, knife, 'cinquième', 'normal')
#     print('Tu vas rentrer dans la salle du boss')
#     boss_room()
#
# def first_floor_light():
#     room('first_floor_light', 'Maraudeur', 12, baseball_bat, 'cinquième', 'faible')
#     print('Tu vas rentrer dans la salle du boss')
#     boss_room()
#
# def first_floor_heavy():
#     room('first_floor_heavy', 'Maraudeur', 19, longsword, 'cinquième', 'lourd')
#     print('Tu vas rentrer dans la salle du boss')
#     boss_room()
#
# def boss_room():
#     room('first_floor_heavy', 'Maraudeur', 19, longsword, 'cinquième', 'lourd')
#     print('Veux tu vas rentrer dans la salle du boss')
#     print('Tu as gagner, gg')
#     input("> ")
#
# def trapped_room():
#     Player().death()
#
# def two_choice(room_one, room_two):
#     while (1):
#         option = input("> ")
#         if (option == 'Gauche'):
#             room_one()
#             break
#         elif (option == 'Droite'):
#             room_two()
#             break
#         else:
#             print('Mauvaise Commande')
#
# def room(enemy_type, enemy_name, enemy_hp, enemy_weapon, room_nb, enemy_strngt):
#     print('Tu arrives dans la', room_nb, 'salle. Il y a un enemie ', enemy_strngt)
#     enemy_type = Enemy('enemy_name', enemy_hp, enemy_weapon)
#     player = Player()
#     print("L'enmie a", enemy_type.health, "hp; Tu as", player.health, "hp")
#     print('Que veux tu faire ?')
#     while (player.health > 1 or enemy_type.health > 1):
#         option = input("> ")
#         if option == "Attaquer":
#             player.attack(enemy_type)
#             print('Tu as infligé', player.current_attack, "points de dégats")
#             print("L'ennemie a", enemy_type.health, "HP")
#             if (enemy_type.health <= 0):
#                 player.win_room()
#                 break
#             enemy_type.attack_enemy(player)
#             print("L'enemie t'as infligé", enemy_type.attack, "points de dégats")
#             print('Tu as', player.health, "HP")
#             if (player.health <= 0):
#                 player.death()
#         else:
#             print('Mauvaise commande')


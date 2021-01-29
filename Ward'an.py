import random
import array
import os
import cmd
import sys
os.system("color 5")

#Le jeu manque encore de beaucoup d'ajouts et d'une séparation des classes dans plusieurs fichiers
#Les armes sont implémentées, mais l'inventaire et le shop ont encore quelques soucis
#Il n'y a pas de directions à prendre pour le moment, le jeu est linéaire

#Liste des armes ennemies (dois être arrangé)
baseball_bat = random.randint(6, 11)
knife = random.randint(12, 18)
longsword = random.randint(17, 22)
Axe = random.randint(19, 25)
Katana = random.randint(20, 28)

class Item: #Objet permettant de créer les armes du joueur qui seront disponibles dans le shop
	def __init__(self, name, damage, value):
		self.name = name
		self.damage = damage
		self.value = value

class Inventory: #Inventaire du joueur, et création des items, encore quelque peu instable et pas propre
	def __init__(self):
		self.items = {}
	def add_item(self, item): #fonction permettant l'ajout des items pour la fonction print en dessous
		self.items[item.name] = item
	def print_items(self): #fonction permettant d'afficher les items
		print('\t'.join(['Name', 'Damage', 'Value']))
		for item in self.items.values():
			print('\t'.join([str(x) for x in [item.name, item.damage, item.value]]))
		print(self.items)

inventory = [] #liste des armes du joueur qu'il pourra acheter et posséder
inventory.append(Item('Poing Américain', 8, 20))
inventory.append(Item('Kukri', 11, 35))
inventory.append(Item('Nunchaku', 14, 50))
inventory.append(Item('Pied de Biche', 17, 70))
inventory.append(Item('Matraque', 20, 100))

shop = Inventory() #Liste des armes qui s'afficheront dans la fonction print_items
shop.add_item(Item('Poing Américain', 8, 20))
shop.add_item(Item('Kukri', 11, 35))
shop.add_item(Item('Nunchaku', 14, 50))
shop.add_item(Item('Pied de Biche', 17, 70))
shop.add_item(Item('Matraque', 20, 100))




class Player:   #Classe du joueur
	def __init__(self):
		self.won_game = 0 #Vérifier si le joueur à gagner
		self.name = '' #Nom du joueur ajouter avec un input
		self.max_health = 30 #Santé max du joueur
		self.health = self.max_health #Santé actuelle du joueur
		self.base_attack = 10 #Attaque de base du joueur
		self.current_wp = 'Matraque' #Arme actuelle du joueur
		self.exp = 10 #Expérience du joueur
		self.armor = 1 #Armure du joueur
		self.balance = 25 #Argent du joueur
	def attack(self, enemy): #Fonction attaquer
		random_attack = random.randint(1, 8)
		if (random_attack == 1): #Condition qui permet que le joueur puisse manquer son coup (basé sur random.randint)
			print("Tu as manqué ton coup !")
		else:
			enemy.health -= self.current_attack #Attaqueur du joueur.
			print('Tu as infligé', self.current_attack, 'points de dégats')
			print("Le", enemy.name, "à", enemy.health, "HP !")
	def death(self): #Fonction si le joueur meurt
		print('Coucou je suis la fonction death')
		print('Tu es mort')
	def win_room(self): #Fonction si le joueur gagne le combat (gagne la salle)
		self.health = 30 #Remettre la vie du joueur à 30 après chaque room
		exp_won = random.randint(32, 47) #combien d'éxpérience le joueur gagne si il gagne le combat
		balance_won = random.randint(5, 40)
		self.balance += balance_won
		self.exp += exp_won #Ajout de l'xp au joueur
		print('-' * 60)
		print('Tu as vaincu cet ennemi !')
		print('Tu as gagné', exp_won, "points d'EXP !" )
		print('Tu as gagné', balance_won, 'Eurodollars')
		print('Tu as', self.exp, "XP !")
		print('Tu as', self.balance, 'Eurosdollars')
		if (self.exp > 400):
			self.won_game = 1
	def game_win(self): #Fonction si le joueur tue le boss et gagne le jeu
		print('*' * 64)
		print('GG ! Tu as finis notre jeu')
		print('Tu avais', self.exp, 'XP !')
		print('Tu avais', self.balance, 'eurodollars !')
		print("Merci d'avoir joué à notre jeu !")
	def parry(self): #Fonction pour que le joueur puisse prendre moins de dégats au prochain tour
		self.armor = (random.randint(0, 30)) / 100  #L'armure du joueur est random entre 0 et 30
		print('Tu as gagné', self.armor, "d'armure pour ce tour")
	def current_dmg(self): #Fonction pour vérifier l'arme et les dégats du joueur chaque tour
		for item in inventory:
			if item.name == self.current_wp:
				self.current_attack = self.base_attack + item.damage

class Enemy: #Class de l'ennemie, les valeurs sont définis en fonction de l'éxpérience du joueur
	def __init__(self, name, maxhealth, attack):
		self.name = name #Nom de l'ennemie
		self.max_health = maxhealth #Santé max de l'ennemie
		self.health = maxhealth #Santé de base de l'ennemie
		self.attack = attack #Attaquer de base de l'ennemie
	def attack_enemy(self, player): #Fonction de l'attaque de l'ennemie
		random_enemy_attack = random.randint(1, 6) #Random de 1 à 6 pour voir si l'ennemie manque son coup
		if (random_enemy_attack == 1): #si l'ennemie rate son coup
			print("L'ennemie à manqué son coup !")
		else: #Attaque de l'ennemie
			enemy_damage = round(self.attack * player.armor) #Dégats de base de l'ennemie divisé par l'amure du joueur
			player.health -= enemy_damage
			print("L'ennemi t'as infligé", enemy_damage, "points de dégats !")
			print("Tu as", player.health, "HP !")
			player.armor = 1 #On remets l'armure du joueur à 1 au cas ou il ai utilisé parry et remettre l'armure à 0

class Room: #Class qui définis l'ennemie de la room
	def __init__(self, enemy_one):
		self.enemy = enemy_one

class Jeu: #Classe du jeu, regroupant la création de la room des ennemies et du joueur
	def __init__(self, player_one):
		self.room = None
		self.player = player_one
		self.generate_room()
	def generate_room(self): #Fonction de création de la room
		player_exp = self.player.exp
		self.description()
		# print('Ou veux tu aller ?')
		# option = input('> ')                      #Code à développer, permettant de choisir à gauche ou à droite
		# if (option == 'Gauche'):                  #Modifiant les chances de tomber sur du loot ou un ennemie
		#    room_type = random.randint(1,30)       #Le loot n'étant pas encore ajouté, ce bout de code ne sert à rien
		# elif (option == 'droite'):                #Ne marche absolument pas pour l'instant
		#     room_type = random.randint(1, 30)
		if (player_exp >= 0 and player_exp < 100): #Création de l'ennemie dans la room en fonction de l'éxpérience du joueur
			enemy_weak = Enemy('Maraudeur', 12, baseball_bat)
			self.room = Room(enemy_weak)
		elif (player_exp >= 100 and player_exp < 200):
			enemy_normal = Enemy('Maraudeur', 16, knife)
			self.room = Room(enemy_normal)
		elif (player_exp >= 200 and player_exp < 300):
			enemy_heavy = Enemy('Maraudeur', 19, longsword)
			self.room = Room(enemy_heavy)
		elif (player_exp >= 300 and player_exp < 400):
			enemy_miniboss = Enemy('Miniboss', 26, Axe)
			self.room = Room(enemy_miniboss)
		elif (player_exp >= 400 and player_exp < 500):
			enemy_boss = Enemy('Boss', 30, Katana)
			self.room = Room(enemy_boss)
	def description(self):
		player_exp = self.player.exp
		self.lieu_1 = 'Tu rentres dans une ruelle'
		self.lieu_2 = 'Tu rentres dans la foret'
		self.lieu_3 = 'Tu rentres dans un immeuble'
		self.lieu_4 = 'Tu rentres quelque part'
		self.miniboss = 'Attention ! tu fais façe à un miniboss'
		self.boss = 'Attention ! Tu fais face au boss finale !'
		lieu = random.randint(1 , 4)
		if (player_exp >= 300 and player_exp <= 400):
			print(self.miniboss)
		elif (player_exp >= 400):
			print(self.boss)
		elif (lieu == 1):
			print(self.lieu_1)
		elif (lieu == 2):
			print(self.lieu_2)
		elif (lieu == 3):
			print(self.lieu_3)
		elif (lieu == 4):
			print(self.lieu_4)

def main(): #Fonction du jeu
	print('Quel est ton nom ?')
	Player.name = input('')
	print("Bienvenue", Player.name)
	game = Jeu(Player()) #Création du joueur
	while (game.player.health > 0): #Boucle de la "vie du jeu", si le joueur meurt, la boucle s'arrête
		while(game.room.enemy.health > 0 and game.player.health > 0): #Si l'ennemie ou je joueur meurt, la boucle s'arrête
			game.player.current_dmg() #Vérification des dégats du joueur
			print('Que veux tu faire ? Attaquer ou Parer ?')
			option = input('> ')
			if (option == "Attaquer"):
				game.player.attack(game.room.enemy) #player attaque l'ennemi
			elif (option == "Parer"):
				game.player.parry() #player parry l'ennemie
			else:
				print('Mauvaise commande')
				continue #En cas de mauvaise commande, on recommence la boucle jusqu'à obtenir une bonne réponse de la part du joueur
			if (game.room.enemy.health > 0): #Si l'ennemie à plus de 0hp, il attaquer le joueur
				game.room.enemy.attack_enemy(game.player)
			if (game.player.health <= 0): #Vérifie la vie du joueur
				game.player.death()
		if (game.player.won_game == 1):
			game.player.game_win()
			break
		elif (game.player.health > 0): #Vérifie bien que le joueur est en vie après le combat
			game.player.win_room()   #S'il l'est, lance la fonction win_room et recréer une room avec l'ennemie adaptée
			game.generate_room()

 #Fonction qui lance le jeu




def title_game_options():
	option = input("> ")
	if option.lower() == ("play"):
		main()
	elif option.lower() == ("quit"):
		sys.exit()
	while option.lower() not in ['play','quit']:
		print("Invalid command, please try again.")
		option = input("> ")
		if option.lower() == ("play"):
			main()
		elif option.lower() == ("quit"):
			sys.exit()




def title_game():
	print('#' * 62)
	print("#          Bienvenue dans le monde de          #")
	print("#                   Keller,Pierre,Pautigny                   #")
	print('#' * 62)
	print("                           .: Play :.                  ")
	print("                           .: Quit :.                  ")
	title_game_options()
 
title_game()

# tant qu'il a pas d'arme, tu lui proposes le shop
# tant que le nom de l'arme choisie ne correspond pas à un item du shop
# on repose la question 'quelle arme voulez-vous acheter ?'
# lorsque la question est vite répondue, on print le nom de l'arme choisie

# weapon = 0
#
# print(inventory)
#
# while (weapon == 0):
#     weapon = input('Choisissez une arme de la liste : ')




#for item in inventory:
#    while not (item.name != weapon):
#        print('Pas de correspondance')





# while weapon not in inventory:
#     for item in inventory:
#         if item.name != weapon:
#             weapon = input('Choisissez une arme dans la liste :')

# while weapon not in for item.name in inventory:
#     if item.name !== weapon:
#         weapon = input('Choisissez une arme de la liste : ')

# print('L\'arme choisie est:', weapon)

# while weapon not in {'Poing Américain', 'Kukri', 'Nunchaku', 'Pied de Biche', 'Matraque'}:
#     
# print ("L'arme choisie est :", weapon)
#
# for item in inventory:
#     if item.name == weapon:
#         print("L'arme choisie est :", weapon + '. Elle fait :', item.damage, 'dégats')




#  def shop():
#   print('Bienvenue au shop !')
#   weapon = None
	
#   if (Player.balance <= 0):
#    print('Vous n\'avez pas assez d\'argent')
#  else:
#     print('Voici la liste des armes présentes :')
#     shop.print_items()
#     print('Que voulez-vous acheter ?')


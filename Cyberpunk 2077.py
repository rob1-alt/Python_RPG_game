
import os
import cmd
import time 
import sys
import random
os.system("color 5")

class player:
    def __init__(self):
        self.name = ''
        self.solves = 0
player1 = player()


def title_game_options():
	option = input("> ")
	if option.lower() == ("play"):
		setup_game()
	elif option.lower() == ("quit"):
		sys.exit()
	while option.lower() not in ['play','quit']:
		print("Invalid command, please try again.")
		option = input("> ")
		if option.lower() == ("play"):
			setup_game()
		elif option.lower() == ("quit"):
			sys.exit()


def title_game():
	#print the title and the decs(us :p)
	print('#' * 62)
	print('#          Bienvenue dans le monde de CyberPunk 2077         #')
	print("#                   Keller,Pierre,Pautigny                   #")
	print('#' * 62)
	print("                           .: Play :.                  ")
	print("                           .: Quit :.                  ")
	title_game_options()



def setup_game():



	question1 = "Salut c'est quoi ton petit nom????\n" 
	for character in question1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	player_name = input("> ")
	player1.name = player_name

	question2 = "Mon cher ami " + player1.name + ", comment vas tu ?\n"
	for character in question2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	feeling = input("> ")
	player1.feeling = feeling.lower()

	question3 = "Moi ça va super ! Dis moi " + player1.name + " , est tu prêt à plonger dans ce monde ? \n"
	for character in question3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	why = input("> ")
	player1.why = why.lower()


title_game()
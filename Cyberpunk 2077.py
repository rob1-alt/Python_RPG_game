# from tkinter import *

#Creation de la fenetre de jeu du RPG
# fen = Tk()
# fen.title("RPG")
# fen.geometry("670x450")
# fen.configure(bg="seashell")


# fen.quit = quit
# quit = Button(fen, text="Exit",command=fen.destroy)
# quit.place_configure(x=400,y=200)
# quit.place()

#fermeture de la fenetre/Rafraichissement de la fenetre
# fen.quit = quit
# quit = Button(fen, text="Exit",command=fen.destroy)
# quit.place_configure(x=400,y=200)
# quit.place()

# fen.mainloop()

import cmd
import os
os.system("color 5")
import time 
import sys
import random
screen_width = 200

class player:
    def __init__(self):
        self.name = ''
        self.position = 'ground'
        self.won = False
        self.solves = 0
player1 = player()


def title_screen_options():
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


def title_screen():
	#Prints the pretty title.
	print('#' * 45)
	print('#          Salut à toi mon grand          #')
	print("#          Keller,Pierre,Pautigny         #")
	print('#' * 45)
	print("                 .: Play :.                  ")
	print("                 .: Quit :.                  ")
	title_screen_options()



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

	question3 = "Dis moi " + player1.name + " ,Que viens tu faire ici ? \n"
	for character in question3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	why = input("> ")
	player1.why = why.lower()


title_screen()
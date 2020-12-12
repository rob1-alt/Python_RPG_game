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
import time 
import sys 
import random
screen_width = 200

def title_screen_options():
	#Allows the player to select the menu options, case-insensitive.
	print("""

 ________       ___    ___  ________   _______    ________   ________   ___  ___   ________    ___  __       
|\   ____\     |\  \  /  /||\   __  \ |\  ___ \  |\   __  \ |\   __  \ |\  \|\  \ |\   ___  \ |\  \|\  \     
\ \  \___|     \ \  \/  / /\ \  \|\ /_\ \   __/| \ \  \|\  \\ \  \|\  \\ \  \\\  \\ \  \\ \  \\ \  \/  /|_   
 \ \  \         \ \    / /  \ \   __  \\ \  \_|/__\ \   _  _\\ \   ____\\ \  \\\  \\ \  \\ \  \\ \   ___  \  
  \ \  \____     \/  /  /    \ \  \|\  \\ \  \_|\ \\ \  \\  \|\ \  \___| \ \  \\\  \\ \  \\ \  \\ \  \\ \  \ 
   \ \_______\ __/  / /       \ \_______\\ \_______\\ \__\\ _\ \ \__\     \ \_______\\ \__\\ \__\\ \__\\ \__\
    \|_______||\___/ /         \|_______| \|_______| \|__|\|__| \|__|      \|_______| \|__| \|__| \|__| \|__|
              \|___|/                                                                                        
                                                                                                             
                                                                                                             

""")

 
	option = input("> ")
	if option.lower() == ("play"):
		setup_game()
	elif option.lower() == ("quit"):
		sys.exit()
	elif option.lower() == ("help"):
		help_menu()		
	while option.lower() not in ['play', 'help', 'quit']:
		print("Invalid command, please try again.")
		option = input("> ")
		if option.lower() == ("play"):
			setup_game()
		elif option.lower() == ("quit"):
			sys.exit()
		elif option.lower() == ("help"):
			help_menu()

def title_screen():
	#Clears the terminal of prior code for a properly formatted title screen.
	os.system('clear')
	#Prints the pretty title.
	print('#' * 45)
	print('#  Salut à toi mon grand   #')
	print("#  Keller,Pierre,Pautigny  #")
	print('#' * 45)
	print("                 .: Play :.                  ")
	print("                 .: Help :.                  ")
	print("                 .: Quit :.                  ")
	title_screen_options()

def setup_game():
    os.system('clear')




title_screen()
from tkinter import *

#Creation de la fenetre
fen = Tk()
fen.title("RPG")
fen.geometry("670x450")
fen.configure(bg="seashell")

input 

fen.quit = quit
quit = Button(fen, text="Exit",command=fen.destroy)
quit.place_configure(x=400,y=200)
quit.place()

#Rafraichissement de la fenetre.
fen.mainloop()
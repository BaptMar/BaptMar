from tkinter import *
from Drake import *
from Ennemis import *
from Rooms import *


"""
def func(event):                #appuyer sur <a> affiche le print dans l'invite de commande
    print("touche a pressée")   #utiliser pour gérer l'inventaire
entree = tkinter.entry(app)
entree.bind("<a>")
entree.bind("<Control-Alt-a>", func)
entree.bind("<Double-Button-1>")            #double clic
entree.bind("<Key>")                        #n'importe quelle touche
entree.pack()
"""

def error_msg():    #message d'erreur au cas où
    messagebox.showerror("ERREUR", "Vous avez fait planter notre jeu !")

app = Tk()                          #fenetre principale
app.title("Adventure Seeker")       #titre fenetre
app.geometry("640x350")             #taille par défaut
app.minsize(width=640, height=350)  #taille mini, regler en fonction des boutons
#app.iconbitmap("icone.ico")        mettre l'icone dans le même dossier
app.config(background="grey")           #voir quoi mettre plus tard

frame_stats = Frame(app)            #bloc de tout sauf barre de saisie

perso = Listbox(frame_stats, width=15, height=10)
perso.insert(1, "DRAKE")
perso.insert(2, "{}".format(Drake.getPV))
perso.insert(3, "{}".format(Drake.getArme))

ennemi = Listbox(frame_stats, width=15, height=10)          #affiche les données de l'ennemi affronté
ennemi.insert(1, "{}".format(Ennemi().getNomEnmi()))
ennemi.insert(2, "{}".format(Ennemi().getPvEnmi()))
ennemi.insert(3, "{}".format(Ennemi().getDgEnmi()))

texte = Label(app, width=60, height=20, borderwidth=1, relief="solid")

piece = Text(texte, width=60, height=1)
piece.insert(INSERT, Room("Atoum").getNomRoom())

action = Text(texte, width=60, height=19)            #affiche le texte du jeu #verifier que ca marche
action.insert(INSERT, "ACTION")

inventaire = Listbox(app, width=15, height=20)    #30 de hauteur
inventaire.insert(1, "INVENTAIRE")

saisie = Entry(app, width=60)

#police d'écriture
Font = ("Calibri", 10)
perso.config(font = Font)
ennemi.config(font = Font)
texte.config(font = Font)
inventaire.config(font = Font)
saisie.config(font = Font)

frame_stats.grid(row=0, column=0)
perso.pack()
ennemi.pack()
texte.grid(row=0, column=1)
piece.pack(side="top")
action.pack(side="bottom")
inventaire.grid(row=0, column=2)
saisie.grid(row=2, column=1)

app.mainloop() #garde la fenetre ouverte. GARDER A LA FIN

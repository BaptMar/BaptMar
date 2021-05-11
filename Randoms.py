import random
from Rooms import *
from Ennemis import *
from b import *
from Drake import *
#from ScriptEgypte import *

class Random():

    #fuite
    def fuite(self):
        nb = random.randint(1, 2)
        if nb == 1:
            print("fuit")
        else:
            print("passe tour")

    #diminution proba sauriens
        #appliquer à chaque récupération de totem
    def ProbaMoins(self):       #diminue la proba d'apparition des sauriens à mesure qu'on récolte des totems
        if room in [sauriens1, sauriens2, sauriens3, sauriens4, gardes1, gardes2]:      #ajouter la neutralisation des créatures à totem
            nbtotem = 1 #virer une fois la variable ajoutée dans le jeu
            Ennemi().setEnnemi(proba=-25) #=-nbtotem*25
        else:
            pass

    #proba apparition Ennemi
    def RollOutEnnemi(self):        #lance les dés pour l'apparition d'un ennemi
        Nmi = piece.getEnnemiRoom()
        nb = random.randint(1, 100)
        if nb in range(1, Nmi.getProba()):     #prendre la proba de l'Nmi
            print("Un {} {} s'approche de Drake".format(Nmi.getNomEnmi(), self.description()))
            #on attribut à Nmi les données d'un mob possédant lui-même des attributs persos appliqué à Ennemi(). on applique ensuite la fonction getNomEnmi à Nmi pour récupérer son nom pius on appelle la description du mob par description() qui est indépendant du reste
        else:
            pass

    #message d'ennemi en approche
    def description(self):
        nb = random.randint(1, 9)
        if nb==1:
            desc="à l’air sournois"
        elif nb==2:
            desc="les yeux injectés de sang"
        elif nb==3:
            desc="plus gros qu’un ours"
        elif nb==4:
            desc="assez dégoûtant"
        elif nb==5:
            desc="qui titube comme ma grand-mère"
        elif nb==6:
            desc="plutôt pathétique"
        elif nb==7:
            desc="tout sauf inoffensif"
        elif nb==8:
            desc="sortant sûrement de prison"
        elif nb==9:
            desc="de mauvaise humeur"
        return desc


#ancienne version
"""def RollOutEnnemi(self):        #lance les dés pour l'apparition d'un ennemi
    if piece.getEnnemiRoom()!="ennemi de la room":
        Nmi = piece.getEnnemiRoom()
        nb = random.randint(1, 100)
        if nb in range(1, Nmi.getProba()):     #prendre la proba de l'Nmi
            print("Un {} {} s'approche de Drake".format(Nmi.getNomEnmi(), self.description()))
            #on attribut à Nmi les données d'un mob possédant lui-même des attributs persos appliqué à Ennemi(). on applique ensuite la fonction getNomEnmi à Nmi pour récupérer son nom pius on appelle la description du mob par description() qui est indépendant du reste
        else:
            pass
    else:
        pass"""

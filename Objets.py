from ScriptEgypte import *

class Objet:
    def __init__(self, nom="Nom", soin=0, dg=10):
        self.__nom = nom
        self.__soin = soin
        self.__degats = dg

#soins
eau = Objet(nom="Bouteille d'eau", soin=20)
bandages = Objet(nom="Bandages", soin=80)

#armes
torche = Objet(nom="Torche", dg=15)
gun = Objet(nom="Pistolet", dg=80)
machette = Objet(nom="Machette", dg=20)
epee = Objet(nom="Épée", dg=50)

#objets trouvable au sol. lancé de dés à chaque entrée dans une pièce

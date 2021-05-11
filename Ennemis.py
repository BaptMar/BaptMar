from Drake import *
from b import *
from Rooms import *
from Randoms import *
#from ScriptEgypte import *

class Ennemi:
    def __repr__(self):
        return "{}|{}|{}|{}".format(self.__nom, self.__vie, self.__degats, self.__proba)

    def __init__(self, nomEnmi="Nom ennemi", pvEnmi=100, dgEnmi=100, proba=0):
        self.__nom = nomEnmi
        self.__vie = pvEnmi
        self.__degats = dgEnmi
        self.__proba = proba       #proba d'apparition

    def getNomEnmi(self):
        return self.__nom
    def getPvEnmi(self):
        return self.__vie
    def getDgEnmi(self):
        return self.__degats
    def getProba(self):
        return self.__proba

    def setEnnemi(self, nomEnmi, pvEnmi, dgEnmi, proba):
        self.__nom = nomEnmi
        self.__vie = pvEnmi
        self.__degats = dgEnmi
        self.__proba = proba

    def attaque(self):
        Drake().setPV(self.__degats)

#egypte
crocodile = Ennemi("Crocodile", 150, 90, 80)
chat = Ennemi("Chat", 20, 10, 5)
chacal = Ennemi("Chacal", 80, 40, 50)
scorpion = Ennemi("Scorpion", 100, 100, 50)
serpent = Ennemi("Serpent", 70, 40, 50)
lion = Ennemi("Lion", 100, 100, 10)
ombre = Ennemi("Ombre", 100, 30, 80)

#chateau
ghoule = Ennemi("Ghoule", 100, 40, 30)
poltergheist = Ennemi("Poltergheist", 100, 40, 30)
hibou = Ennemi("Hibou", 30, 20, 10)

#jungle
saurien1 = Ennemi("Saurien", 100, 50, 25)
saurien2 = Ennemi("Saurien", 100, 50, 50)
saurien3 = Ennemi("Saurien", 100, 50, 75)
saurien4 = Ennemi("Saurien", 100, 50, 100)
gardesaurien = Ennemi("Garde saurien", 100, 50, 100)
araignee = Ennemi("Araignée géante", 100, 100, 100)
piranha = Ennemi("Piranhas", 50, 70, 80)
singe = Ennemi("Singe", 80, 70, 100)
panthere = Ennemi("Panthère noire", 90, 80, 100)

#mausolée
chauvesouris = Ennemi("Chauve-souris", 20, 10, 10)

#vaisseau
zombie = Ennemi("Alien zombie", 20, 60, 60)   #rester immobile pour avoir une chance de lui échapper


#if __name__ == '__main__':

from b import *
from Rooms import *
from Ennemis import *
from Randoms import *
#from ScriptEgypte import *

class Drake:
    def __repr__(self):
        return "Drake|{}|{}".format(self.__pv, self.__arme)

    def __init__(self, pv=100, arme="À la merci des éléments", objet="Pas d'objet"):
        self.__pv = pv     #voir pour mettre vie max
        self.__arme = arme

    def getPV(self):
        return self.__pv
    def getArme(self):
        return self.__arme

    def setPV(self, vie):
        self.__pv = pv
    def setArme(self, dg):  #attribué en double cliquant sur une arme dans l'inventaire
        self.__arme = dg

    def blessure(self, dg=5):
        self.__pv -= dg
    def soin(self, PV):
        self.__pv += PV

if __name__ == '__main__':
    print(Drake())

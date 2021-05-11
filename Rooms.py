from Ennemis import *
from b import *
from Randoms import *
from Ennemis import *
from Rooms import *
from Drake import *
#from ScriptEgypte import *

class Room:
    def __repr__(self):
        return "{}|{}".format(self.__nom, self.__ennemi)

    def __init__(self, nomRoom="nom room", ennemiRoom="ennemi de la room"):
        self.__nom = nomRoom
        self.__ennemi = ennemiRoom

    def getNomRoom(self):
        return self.__nom
    def getEnnemiRoom(self):
        return self.__ennemi

#egypte
atoum = Room("Atoum")
thot = Room("Thot")
bastet = Room("Bastet", chat)
nil = Room("Nil", crocodile)
jugement = Room("Salle du jugement")
osiris = Room("Osiris", scorpion)
isis = Room("Isis")
nephtys = Room("Nephtys", serpent)
seth = Room("Seth", chacal)
horus = Room("Horus")
apophis = Room("Ténèbres d'Apophis", ombre)

#chateau
entree = Room("Entrée", hibou)
bibliotheque = Room("Bibliothèque", False)
couldom = Room("Couloir des domestiques", False)
chambredom1 = Room("Chambre de domestique 1", False)
chambredom2 = Room("Chambre de domestique 2", False)
chambredom3 = Room("Chambre de domestique 3", False)
reposdom = Room("Salle de repos des domestiques", False)
manger = Room("Salle à manger", False)
cuisine = Room("Cuisine", False)
ptitsalon = Room("Petit salon", False)
mezzanine = Room("Mezzanine", hibou)
galerie = Room("Galerie", False)
terrassegal = Room("Terrasse de la galerie", hibou)
musee = Room("Musée", False)
terrassemus = Room("Terrasse du musée", hibou)
salon = Room("Salon", False)
chambre = Room("Chambre", False)
bureau = Room("Bureau", False)
grenier = Room("Grenier", False)

#jungle
lisiere = Room("Lisière", True)
sauriens1 = Room("Jungle", False)
sauriens2 = Room("Jungle", False)
totemserpent = Room("Clairière", False)
piege1 = Room("Fleuve", False)
piranhas1 = Room("Fleuve sanguinolant", False)
singes = Room("Arbres aux singes", False)
serpents = Room("Nid de serpents", False)
piranhas2 = Room("Fleuve sanguinolant", False)
sauriens3 = Room("Jungle", False)
totemsinge = Room("Clairière", False)
piege2 = Room("Jungle", False)
sauriens4 = Room("Jungle", False)
piege3 = Room("Fleuve", False)
totempanthere = Room("Clairière", False)
totemaraignee = Room("Fleuve peu profond", False)
araignees = Room("Toiles", False)
pantheres = Room("Jungle", False)
piranhas3 = Room("Fleuve sanguinolant", False)
gardes1 = Room("Jungle", False)
gardes2 = Room("Jungle", False)
temple = Room("Temple", True)

#mausolée


#vaisseau
reception = Room("Salle du téléporteur", True)

garage = Room("Baie des vaisseaux", True)

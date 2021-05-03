#Les intéractions de combat vont ici.

#Les intéractions de combat vont ici.

#Création de la classe armes, avec stats.
class Armes ():
    def __init__(self, nomArme="Vieux Revolver", dgArme=3):
        self.__nom = nomArme
        self.__dg = dgArme

    def GetNom (self):
        return self.__nom

    def SetNom (self,NomArme):
        self.__nom = NomArme

    def GetDg (self):
        return self.__dg
    
    def SetDg (self,DgArme):
        self.__dg = DgArme
#Création de la classe et variable du personnage
class Personnage():
    def __init__(self, name, vie=100,nomArme="Vieux Revolver", dgArme=3, armor=0):
        self.__nom = name
        self.__vie = vie
        self.__armes = Armes(nomArme, dgArme)
        self.__armor = armor
    

#De quoi récupérer les noms, PV et Mana des persos (ennemies et notre perso inclus)

    def GetNom(self):
        return self.__nom

    def GetPv(self):
        return self.__vie
    
    def GetMana(self):
        return self.__mana
    
#Mini programmes pour les actions Recevoir des dégâts, FAIRE des dégâts, et CHECK qu'on est en vie.
    def RecevoirDegats (self,degats,armor):
        self.__vie = self.__vie - (degats - armor)
        if self.__vie <= 0:
            self.__vie = 0

    def attaquer (self, Cible):
        Cible.RecevoirDegats(self.__armes.GetDg())
    
    #Créer un def pour un menu d'objet.


    #Check si tu est vivant.
    def IsAlive (self):
        if self.__vie <= 0:
            return True
        else:
            return False

#Un string qui résume le nom, PV, Mana restant, avec le nom de l'arme et ses stats) et la status du perso (mort/Vivant)

    def __str__(self):
        return "{} | PV : {} (armure:{})| Arme : {} (dg {}) | {}".format(self.__nom,self.__vie,self.__armor,self.__armes.GetNom(),self.__armes.GetDg(),"Mort" if(self.IsAlive()) else "Vivant")


#A faire : Créer une chaine de combat qui récupère nos persos (plusieur ou solo), les ennemies (plusieur possible.), un choix de qui on attaque,
#Une chaine d'action, l'ordre pour l'instant sera nos persos, puis l'ennemi. 
#Optionnel:On pourra ajouter un stat vitesse pour faire un ordre croissant.)

import time
import random
from Drake import *
from Rooms import *
from Ennemis import *
from Randoms import *
from Trucs import *

#ajouter le lancé de dés d'apparition d'ennemis après les choix impliquant un mouvement
#ajouter les lignes pour s'assurer de la bonne saisie
#voir pour attribuer une touche à l'inventaire

#Drake est face au Sphinx qui lui pose une enigme
    #protéger des mauvaises saisies
print("J'accepte ton défi Sphinx, énonce ton énigme")
time.sleep(1)
reponse = str(input("Qu'es-ce qui est petit et marron ?\n"))
if reponse == "un marron":    #synthaxe 1, ajouter les autres cas dans les crochets
    time.sleep(2)
    print("Putain il est fort ce con")
    time.sleep(1)
else:
    while reponse != "un marron":   #synthaxe 2, à répéter en entier espacé de or pour chaque cas si plusieurs
        reponse = str(input("Faux\n"))
time.sleep(1)
print("Félicitations noble guerrier. Tu t'es montré digne d'admirer la relique sacrée")
#Drake entre dans le champ de roseaux


piece = atoum
print("Drake sort de l’eau et se retrouve dans une salle plongée dans le noir le plus total. Elle est également remplie d’eau lui arrivant aux genoux")
time.sleep(4)
choix = input("Propositions :\n- Avancer à l'aveugle\n")

while True:
    if choix == "avancer":
        print("Drake avance au hasard dans l'obscurité\nIl se rétame. -5PV\n")
        Drake().blessure()
        choix = input()
    if choix == "briquet":    #DOUBLE CLIC INVENTAIRE
        print("Drake sort son briquet et l'allume") #continue
        break
    choix = input("Action invalide\n")

time.sleep(1)
print("La faible lueur de son briquet peine à percer les épais ténèbres autour de lui. Il a toujours beaucoup de mal à distinguer son environnement proche mais comprend néanmoins qu'il se trouve dans une vaste grotte souterraine partiellement indondée, visiblement seul. Il distingue une énorme sphère suspendue à plusieurs mètres du sol devant lui ainsi qu'un mur sur sa gauche")
time.sleep(5)
choix = input("Propositions :\n- Etudier la SPHERE\- Etudier le MUR\n")
while True:
    if choix == "mur":
        print("Drake se dirige vers le mur. Il distingue de nombreux hiéroglyophes gravés il y a des milliers d'années")
        time.sleep(4)
        choix = input("Propositions :\n- ETUDIER les hiéroglyphes\n- Retourner à la SPHERE\n")
        while True:
            if choix == "etudier":
                print("En approchant le briquet pour lire, la porte émet un léger grondement sourd. Les hiéroglyphes racontent la cosmogonie égyptienne héliopolitaine. «Atoum, le dieux solaire, émergea de l’océan Noun pour explorer Temtem, la première terre émergée nouvellement apparue. Il illumina le Grand Rien en créant le soleil puis donna naissance à ses deux enfants, Shou, le vent, et Tefnout, l’humidité...»")
                time.sleep(5)
                choix = input("Propositions :\n- CONTINUER la lecture\n- Retourner à la SPHERE\n")
                if choix == "continuer":
                    print("«...ses enfants partirent explorer le Noun. Inquiet, Atoum partit à leur recherche et finit par les retrouver. Il en fût tellement soulagé qu’il pleura toutes les larmes de son corps. Ces dernières prirent vie et devinrent les premiers humains»")
                    time.sleep(5)
                    print("Bon allez c’est pas tout ça mais j’ai du boulot moi")
                    time.sleep(5)
                    i = 0
                    break
                elif choix == "sphere":
                    break
            elif choix == "sphere":
                break
            if i == 0:
                break
            choix = input("Action invalide\n")
    if choix == "sphere" or i == 0:    #DOUBLE CLIC INVENTAIRE
        while True:
            print("Drake se dirige vers la sphère suspendu. En s'approchant, il réalise qu'elle n'est pas suspendu mais qu'elle lévite à environ 7 mètres du sol. Une fois en dessous du globe, le sol se met à trembler sous l'eau. Soudain, un morceau de roche pyramidal pousse sous les pieds de Drake qui parvient à s'accrocher. En quelques secondes, tout s'est arrêté. Drake regarde autour de lui et constate qu'il se trouve maintenant à plus de 5 mètres de l'eau. La sphère n'est plus qu'à dizaines de centimètres de sa tête en se tenant debout. En étudiant la surface de la sphère, il a l'impression de regarder une sorte de soleil éteint. Comme les photos solaires de la NASA mais en noir et blanc")
            choix = input("Propositions :\- Approcher le BRIQUET de la sphère")
            while True:
                if choix == "briquet":
                    i = 1
                    break
                choix = input("Action invalide\n")
            if i == 1:
                break
            choix = input("Action invalide\n")
        if i == 1:
            break
    if i == 1:
        break
    choix = input("Action invalide\n")

print("Au contact de la flammèche, la sphère s’embrase subitemment pour illuminer toute la pièce. Elle ressemble maintenant à un véritable soleil")
time.sleep(3)
if lunettes == 1:                                                                  ################################
    print("Drake descend de la pyramide et se retourne pour admirer le soleil miniature. Il met son poing sur son cœur en prend une grande inspiration\n«Allumeeeeeeez le feu !»\nAu même moment, il entend derrière lui un bruit de mécanisme venant du mur de tout à l'heure. Il constate qu'il s'est ouvert et donne sur un long couloir")
    time.sleep(5)
    choix = input("Propositions :\n- PARTIR explorer le tombeau\n- CHANTER «Allumez le feu»\n")
    while True:
        if choix == "chanter":
            Johnny1()                                                              ################################
            choix = input("Propositions :\n- ENCHAINER sur «»\n- PARTIR\n")        ################################
            while True:
                if choix == "enchainer":
                    print("Allez tous avec moi !")
                    time.sleep(2)
                    Johnny2()                                                      ################################
                    time.sleep(5)
                    print("Pfiou... quelle chaleur. Bon allez c’est pas tout ça mais les trésors vont pas se pill- se découvrir tout seuls")
                    i = 2
                    break
                elif choix == "partir":
                    i = 2
                    break
                choix = input("Action invalide\n")
            if i == 2:
                break
        elif choix == "partir":
            break
        choix = input("Action invalide\n")
    time.sleep(5)
else:
    print("La lumière atomise instantanément les rétines de Drake qui perd l’équilibre et dégringole de la pyramide. Il s'écrase au sol puis passe plusieurs minutes à gémir et se rouler en boule de douleur\n«Haaaaa le cooon ! J’avais des lunettes de soleil en plus !»\nUne fois remit du choc, il réalise que l’eau a disparu")
    time.sleep(5)
    count = 0
    while count < 3:
        choix = input("Propositions :\n- RAMPER\n")
        count += 1
    print("Maintenant, les yeux de Drake parvienent à nouveau à distinguer des formes. Il voit que le mur s'est ouvert sur un long couloir. Il se redresse péniblement et se traîne hors de la grotte")
    time.sleep(5)
    print("Pendant qu'il avance, il sent la terre vibrer à nouveau. Cette fois, c'est comme si une énorme masse se mouvait à plusieurs dizaines de mètres en-dessous")
    time.sleep(5)

piece = nil
print("Drake avance de quelques mètres avant de se retrouver au bord d'un fleuve souterrain. Il voit des formes sombres bouger sous la surface légérement agitée et trouble. Inhabituelle pour une eau sousterraine... En levant le nez, il aperçoit plusieurs portes dans les murs latéraux. Elles sont toutes uniquement accessibles par l'eau sauf les deux plus proches")
time.sleep(5)
choix = input("Propositions :\n- Essayer la porte de GAUCHE\n- Essayer la porte de DROITE\n- PLONGER dans le fleuve")
while True:
    if choix == "plonger":
        Random().RollOutEnnemi()
    #if
        #sequence de combat
    if choix == "gauche":
        piece = thot
        #thot stuff
    if choix == "droite":
        piece = bastet
        Random().RollOutEnnemi()
        #bastet stuff

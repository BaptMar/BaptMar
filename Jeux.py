#Le code principale du jeux vient ici.

#import Pool_Event_1 from Pool_Event_1

#Trouver un moyen d'importer le pool qu'on veut quand on le veut, tout en enlevant l'ancien 
#pour éviter d'overlap.
#Difficulty = 0  (1 = Easy, 2 = normal, 3 = hard. Affecte les stats et le nombre d'events.)
Level = 1
EnemyPool = 0
EventPool = 0
RandomEvents = 0
ObligatoryEvent = 0
EventCounter

#Le menu du jeu, contient le game start, et un quit pour le jeu. (Optionnel:Reprise du jeu, mais bon.)
print("Ruins Seeker\n\n1. Commencer un périple\n2. Tutoriel\n\n3. Credits\n4. Rebrousser chemin")
Menu = int(input('')

while True:
    try:
        if Menu == 1:
            #Début du jeu dans l'autre bloc de commande.
        if Menu == 2:
            #Tutoriel ici
        if Menu == 3:
            print("Made and developped by Anthony Tran and Baptiste Martin.\nFor the substitution project of our first year at EPSI.")
            #Ajoute plus de texte si tu veut dire des choses dans les crédits.
        if Menu == 4:
            exit()
        if Menu <= 0:
            print("Erreur, choix érronée.")
        if Menu >= 6:
            print("Erreur, choix érronée.")
    except:
        print("Erreur, choix érronée.")

#Configuration du niveau 1 (set d'abord les pools, optionnelement le nombre d'event avec une difficulté.)
if Level == 1:
    EnemyPool = 1
    EventPool = 1
    RandomEvents = 3
    ObligatoryEvent = 0
    #if difficulty == 1
    #   RandomEvents = 2
    #if difficulty == 2
    #   RandomEvents = 3
    #if difficulty == 3
    #   RandomEvents = 4

#Prototype du jeu. Abuse de "continue" et ajoute un variable à chaque event obligatoire pour dire que c'est fait.
#pour l'instant, on fait la vérification des events obligatoire par tier 
#(event 1 fait(Pas forcément réussi)? ObligatoryEvent = 1. 2e event obligatoire fait? ObligatoryEvent = 2 etc.)

#Le premier while est pour mettre tout les events obligatoire, le second while à l'intérieur est un
#repeat qui fait les events RNG en prenant un event, le complétant puis en ajoutant +1 à un compteur jusqu'à
#ce que le compteur == RandomEvents. Evidemment remis à 0 entre chaque niveau.

#Remarque : Ce système va devoir faire répéter le bloc de commande des obligatory event à chaque niveau. à améliorer.
while True:
    try:
        if ObligatoryEvent == 0:
            #Event obligatoire début LVL 1
            print("Ajoute l'event d'intro de Baptiste ici.")
            ObligatoryEvent = ObligatoryEvent + 1
            #TidBit, les récompenses seront en après event, par exemple
            #GetHP = GetHP + 10 etc.
            #M O N E Y = M O N E Y + 1000000$
            continue
        elif ObligatoryEvent == 1:
            #Event obligatoire fin LVL 1
            print("Ajoute l'event de fin LVL1 (ou milieu LVL1, ce que tu veut.)")
            ObligatoryEvent = ObligatoryEvent + 1
            continue
    except:
        print("Cyka blyat le 1er while s'est cassée.")

#Le second while à mettre dans le 1er while des events obligatoires. A voir où le placer.
while True:
    try:
        if EventCounter == RandomEvents:
            break
        if Level == 1
            #Insère le code de RNG pour choisir un nombre entre "LimDébutListeEvent" et "LimFinListeEvent"
            EventCounter = EventCounter + 1
            continue
        if Level == 2
            #Insère le code de RNG pour choisir un nombre entre "LimDébutListeEvent" et "LimFinListeEvent"
            EventCounter = EventCounter + 1
            continue
        if Level == 3
            #Insère le code de RNG pour choisir un nombre entre "LimDébutListeEvent" et "LimFinListeEvent"
            EventCounter = EventCounter + 1
            continue
        if Level == 4
            #Insère le code de RNG pour choisir un nombre entre "LimDébutListeEvent" et "LimFinListeEvent"
            EventCounter = EventCounter + 1
            continue
        if Level == 5
            #Insère le code de RNG pour choisir un nombre entre "LimDébutListeEvent" et "LimFinListeEvent"
            EventCounter = EventCounter + 1
            continue
        except:
            print("LE 2E WHILE EST MORT AAAAAAAAAH")

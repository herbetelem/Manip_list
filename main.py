def showPairPosition(liste):
    compteur = 0
    result = []
    for index in liste:
        if compteur % 2 == 0:
            result.append(index + " position " + str(compteur))
        compteur += 1
    return result

def changeTheTarget(liste, target, value):
    if isinstance(liste[target], int) and isinstance(value, int):
        liste[target] = value
    elif isinstance(liste[target], float) and isinstance(value, float):
        liste[target] = value
    elif isinstance(liste[target], str) and isinstance(value, str):
        liste[target] = value
    return liste

def addAndRemove(liste, valeur):
    liste.append(valeur)
    del liste[0]
    return liste

import random

def changeRandom(liste, valeur):
    newIndex = random.randint(0, (len(liste) - 1))
    liste[newIndex] = valeur
    return liste

def tellReste(liste, index):
    valeur = liste[index]
    del liste[index]
    reste = liste.count(valeur)
    return "there are still " + str(reste) + " letter " + str(valeur) + "'s"

def mostCommon(liste1, liste2, liste3):
    commonalities = set(liste1) - (set(liste1) - set(liste2))
    nbCom1et2 = len(commonalities)
    
    commonalities = set(liste2) - (set(liste2) - set(liste3))
    nbCom2et3 = len(commonalities)
    
    commonalities = set(liste1) - (set(liste1) - set(liste3))
    nbCom1et3 = len(commonalities)

    if nbCom1et2 > nbCom2et3 and nbCom1et2 > nbCom1et3:
        return "liste 1 et liste 2 on le plus de point commun c'est a dire " + str(nbCom1et2)
    elif nbCom2et3 > nbCom1et2 and nbCom2et3 > nbCom1et3:
        return "liste 2 et liste 3 on le plus de point commun c'est a dire " + str(nbCom2et3)
    if nbCom1et3 > nbCom2et3 and nbCom1et3 > nbCom1et2:
        return "liste 1 et liste 3 on le plus de point commun c'est a dire " + str(nbCom1et3)

def sortListe(liste):
    liste.sort()
    return liste

print(sortListe([8, 4, 5, 63, 78, 12, 0]))
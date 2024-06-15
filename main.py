
# Programme des médaillés des JO
# @Version 1.0
from typing import List

from medaille import Medaille
from athlete import Athlete
from epreuve import Epreuve
from pays import Pays

def choixMenu():
    print("Menu")
    print("1 - Enregistrer un médaillé")
    print("9 - Quitter")
    choix = int(input(" Choix : "))
    while choix != 9 and choix !=1 :
        choix = int(input("Choix : "))
    return choix

def choisirTypeMedaille(lesTypesDeMedailles : List[str]) -> int:
    """
    Permet au joueur de choisir un type de médaille
    :param lesTypesDeMedailles: liste des types de médaille
    :return: l'index du type de médaille choisi
    """
    choix = 0
    while(choix != 1 and choix != 2 and choix != 3):
        for i in range(len(lesTypesDeMedailles)):
            print(str(i + 1) + " : " + lesTypesDeMedailles[i])
        choix = int(input("Saisir un type de medaille :"))
    return choix-1


def creerMedaille(athlete : Athlete,epreuve: Epreuve,type : str) -> Medaille :
    """
    Permet de créer une médaille
    :param athlete: athlete remportant la médaille
    :type athlete: Athlete
    :param epreuve: epreuve concernée par la médaille
    :type epreuve: Epreuve
    :param type: type de la médaille "Or", "Argent","Bronze"
    :type type: string
    :rtype : Medaille
    :return : retourne la médaille remportée par l'athlete passée en paramètre pour l'épreuve passée en paramètre

    """
    return Medaille(type,epreuve,athlete)

#--- PROGRAMME PRINCIPAL ----#
if __name__ == "__main__":

    lesTypesDeMedailles =["Or","Argent","Bronze"]

    choix = choixMenu()
    while (choix !=9):

        if (choix == 1):
            # Enregistrement d'un médaillé
            nom = input("Nom de l'athlete ? ")
            prenom = input("Prenom de l'athlete ? ")
            nomPays = input("Pays de l'athlete ? ")
            langueOff = input("Langue officielle du pays ? ")
            anneePremParti = int(input("Annee première participation aux jeux ? "))
            premierJeu = input("Ville des premiers jeux ? ")
            epreuve = input("Intitule de l'epreuve ? ")
            itypeMed = choisirTypeMedaille(lesTypesDeMedailles)

            uneMedaille = creerMedaille(Athlete(nom,prenom,Pays(nomPays,langueOff),anneePremParti,premierJeu),Epreuve(epreuve),lesTypesDeMedailles[itypeMed])

            print(uneMedaille)
        choix = choixMenu()


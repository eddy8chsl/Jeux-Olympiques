from __future__ import annotations

import datetime

from pays import Pays

class Athlete :
    #Attributs
    __nom : str
    __prenom : str
    __equipe : Pays # pays de l'athlete
    __premiereParticipation : tuple #(int,str) #(annee de première participation, nom du jeu de la premiere participation)

    def __init__(self, nom: str, prenom : str, equipe: Pays, anneePremParti : int, premierJeu : str):
        self.__nom = nom
        self.__prenom = prenom
        self.__equipe = equipe
        self.__premiereParticipation = (anneePremParti,premierJeu)

    def getEquipe(self) -> Pays:
        return self.__equipe

    def getNom(self) -> str:
        return self.__nom

    def getPrenom(self) -> str:
        return self.__prenom

    def getPremiereParticipation(self) -> tuple:
        return self.__premiereParticipation

    def __str__(self):
        """ Permet de définir le format d'affichage de l'athlete respectant le format suivant :
            prénom_athlete nom_athlete (équipe : nom_equipe - première participation nom_jeu annee_première_participation)
            exemple : "Cyrena SAMBA-MAYELA (équipe : France - première participation Tokyo 2020)"
            :rtype: str
            :return : l'athlete au format str
        """
        return "{0} {1} (équipe : {2} - première participation {3} {4})".format(self.__prenom,self.__nom,self.__equipe.getNom(), self.__premiereParticipation[1], self.__premiereParticipation[0])

    def nbAnneeDepuisPremiereParticipation(self) -> int :
        """
        Permet de savoir le nombre d'années écoulées depuis la première participation aux jeux
        :rtype : int
        return : le nombre d'années écoulées depuis l'année de la première participation aux jeux et l'année courante
        """
        return datetime.date.today().year - self.__premiereParticipation[0]
    
    def __eq__(self, other : Athlete):
        return self.getNom() == other.getNom() and self.getPrenom() == other.getPrenom() and self.getEquipe() == other.getEquipe() and self.getPremiereParticipation() == other.getPremiereParticipation()


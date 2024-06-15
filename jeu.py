from __future__ import annotations

from medaille import Medaille
from athlete import Athlete
from epreuve import Epreuve
from pays import Pays

class Jeu:

    #Attributs
    __annee : int
    __nomlieu : str
    __medailles : list[Medaille]

    def __init__(self, annee : int, nomlieu : str, medaille : list[Medaille]):
        self.__annee = annee
        self.__nomlieu = nomlieu
        self.__medailles = medaille

    def getAnnee(self) -> int:
        return self.__annee

    def getNomLieu(self) -> str:
        return self.__nomlieu

    def getMedailles(self) -> list[Medaille]:
        return self.__medailles

    def ajouterMedaille(self, med : Medaille) -> bool:
        self.__medailles.append(med)
        return True

    def medailleByAth(self, ath : Athlete) -> list[Medaille]:
        l = []
        for i in range(len(self.__medailles)):
            if self.__medailles[i].getAthlete() == ath:
                l.append(self.__medailles[i])
        return l
    
    def classementByEpreuve(self, ep : Epreuve) -> list[Athlete]:
        classement = []
        mbr = ""
        mar = ""
        mor = ""

        for i in range(len(self.__medailles)):
            if self.__medailles[i].getEpreuve() == ep and self.__medailles[i].getType() == "Bronze":
                mbr = self.__medailles[i].getAthlete()
            if self.__medailles[i].getEpreuve() == ep and self.__medailles[i].getType() == "Argent":
                mar = self.__medailles[i].getAthlete()
            if self.__medailles[i].getEpreuve() == ep and self.__medailles[i].getType() == "Or":
                mor = self.__medailles[i].getAthlete()
        
        classement.append(mor)
        classement.append(mar)
        classement.append(mbr)
        return classement

    def medailleByPays(self, monpays : str) -> list[Medaille]:
        list_medaille = []
        for i in range(len(self.__medailles)):
            if self.__medailles[i].getAthlete().getEquipe().getNom() == monpays:
                list_medaille.append(self.__medailles[i])
        return list_medaille

    def nbmedailleByPays(self, monpays : str) -> int:
        nbmedaille = 0
        for i in range(len(self.__medailles)):
            if self.__medailles[i].getAthlete().getEquipe().getNom() == monpays:
                nbmedaille += 1
        return nbmedaille

    def paysAyantLePlusDeMedaille(self) -> list[Pays]:
        list_pays = []
        list_nbmedaille = []
        for i in range(len(self.__medailles)):
            nb_medaille = self.nbmedailleByPays(self.__medailles[i].getAthlete().getEquipe().getNom())
            if self.__medailles[i].getAthlete().getEquipe().getNom() not in list_pays:
                list_pays.append(self.__medailles[i].getAthlete().getEquipe().getNom())
                list_nbmedaille.append(nb_medaille)

        print(list_nbmedaille)
        max_nbmedaille = max(list_nbmedaille)
        return list_pays[list_nbmedaille.index(max_nbmedaille)]

        """
        dict_pays_medailles = {}
        for medaille in self.__medailles:
            pays = medaille.getAthlete().getEquipe().getNom()
            dict_pays_medailles[pays] = dict_pays_medailles.get(pays, 0) + 1

        max_medailles = max(dict_pays_medailles.values())
        
        # Trouver tous les pays ayant le nombre maximum de médailles
        pays_max_medailles = [pays for pays, medailles in dict_pays_medailles.items() if medailles == max_medailles]
        
        return pays_max_medailles"""


    def __str__(self) -> str:
        return "{0} {1} {2}".format(self.getNomLieu(), self.getAnnee(), self.getMedailles())
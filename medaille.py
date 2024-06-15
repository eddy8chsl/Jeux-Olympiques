
from athlete import Athlete
from epreuve import Epreuve

class Medaille:

    #Attributs
    __type : str # type de la médaille (or, argent ou bronze)
    __epreuve : Epreuve # épreuve concernée par la médaille
    __athlete : Athlete # athlete ayant remporté la médaille

    def __init__(self, type : str, epreuve : Epreuve):
        self.__type = type
        self.__epreuve = epreuve
        self.__athlete = None

    def getType(self):
        return self.__type

    def getAthlete(self) -> Athlete:
        return self.__athlete

    def getEpreuve(self) -> Epreuve:
        return self.__epreuve

    def __str__(self):
        return "Epreuve : {0} - Medaille en {1} remportée par {2}".format(self.__epreuve.getIntitule(), self.__type, self.__athlete)

    def attribuer(self, ath : Athlete) -> bool:
        self.__athlete = ath
        return True
        

#End file



class Epreuve:
    #Attributs
    __intitule : str #intitule de l'épreuve

    def __init__(self, intitule: str):
        self.__intitule = intitule

    def getIntitule(self) -> str:
        return self.__intitule

    def __str__(self):
        return "Epreuve : {0}".format(self.__intitule)



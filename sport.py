

class Sport:
    #Attributs
    __nom : str

    def __init__(self,nom :str):
        self.__nom = nom

    def getNom(self):
        return self.__nom

    def __str__(self):
        return "{0}".format(self.getNom())

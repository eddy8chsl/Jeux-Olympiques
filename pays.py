
class Pays:
    #Attributs
    __nom : str # nom du Pays
    __langueOfficielle : str # langue officielle du Pays

    def __init__(self,nom :str, langue : str):
        self.__nom = nom
        self.__langueOfficielle = langue

    def getNom(self):
        return self.__nom

    def getLangueOfficielle(self):
        return self.__langueOfficielle

    def __str__(self):
        return "{0} (langue officielle: {1})".format(self.getNom(), self.getLangueOfficielle())


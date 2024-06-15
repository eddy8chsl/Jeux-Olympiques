import unittest

from athlete import Athlete
from epreuve import Epreuve
from medaille import Medaille
from pays import Pays
from jeu import Jeu


class TestJeu(unittest.TestCase):
    def testclassementByEpreuve(self):
        ep = Epreuve("Women's Street")
        jeu = Jeu(2020, "Tokyo", [])

        ath1 = Athlete("RAYSSA", "Leal", Pays("Brésil", "portugais"), 2020, "Tokyo")
        medaille1 = Medaille("Argent", ep)

        medaille1.attribuer(ath1)
        jeu.ajouterMedaille(medaille1)

        ath2 = Athlete("Romain", "Alicia", Pays("France", "français"), 2020, "Tokyo")
        medaille2 = Medaille("Or", ep)

        medaille2.attribuer(ath2)
        jeu.ajouterMedaille(medaille2)

        ath3 = Athlete("Azerty", "Clara", Pays("Allemagne", "Allemand"), 2020, "Tokyo")
        medaille3 = Medaille("Bronze", ep)

        medaille3.attribuer(ath3)
        jeu.ajouterMedaille(medaille3)

        self.assertEqual([ath2, ath1, ath3],jeu.classementByEpreuve(ep), "Err. classement athlète par medaille")  # add assertion here

    def testCreactionJeu(self):
        ep = Epreuve("Women's Street")
        jeu = Jeu(2020, "Tokyo", [])
        ath3 = Athlete("Azerty", "Clara", Pays("Allemagne", "Allemand"), 2020, "Tokyo")
        medaille3 = Medaille("Bronze", ep)
        medaille3.attribuer(ath3)
        self.assertEqual("Tokyo", jeu.getNomLieu(), "Err. créaction du jeu")

    def testmedaillleByAth(self):
        ep = Epreuve("Women's Street")
        jeu = Jeu(2020, "Tokyo", [])
        ath2 = Athlete("Romain", "Alicia", Pays("France", "français"), 2020, "Tokyo")
        medaille2 = Medaille("Or", ep)

        medaille2.attribuer(ath2)

        self.assertEqual(True, jeu.ajouterMedaille(medaille2), "Err. attribution de medaille")

    def testmedailleByPays(self):
        ep = Epreuve("Women's Street")
        ep2 = Epreuve("Women's Volley Ball")
        jeu = Jeu(2020, "Tokyo", [])

        ath2 = Athlete("Romain", "Alicia", Pays("France", "français"), 2020, "Tokyo")
        medaille2 = Medaille("Or", ep)

        medaille2.attribuer(ath2)
        jeu.ajouterMedaille(medaille2)

        ath1 = Athlete("Voisin", "Clara", Pays("France", "français"), 2020, "Tokyo")
        medaille1 = Medaille("Argent", ep2)

        medaille1.attribuer(ath1)
        jeu.ajouterMedaille(medaille1)

        self.assertEqual([medaille2, medaille1], jeu.medailleByPays("France"), "Err. medaille par pays")

    def testnbmedailleByPays(self):
        ep = Epreuve("Women's Street")
        ep2 = Epreuve("Women's Volley Ball")
        jeu = Jeu(2020, "Tokyo", [])

        ath2 = Athlete("Romain", "Alicia", Pays("France", "français"), 2020, "Tokyo")
        medaille2 = Medaille("Or", ep)

        medaille2.attribuer(ath2)
        jeu.ajouterMedaille(medaille2)

        ath1 = Athlete("Voisin", "Clara", Pays("France", "français"), 2020, "Tokyo")
        medaille1 = Medaille("Argent", ep2)

        medaille1.attribuer(ath1)
        jeu.ajouterMedaille(medaille1)

        ath3 = Athlete("Chasle", "Nadia", Pays("France", "français"), 2020, "Tokyo")
        medaille3 = Medaille("Bronze", ep)

        medaille3.attribuer(ath3)
        jeu.ajouterMedaille(medaille3)

        self.assertEqual(3, jeu.nbmedailleByPays("France"), "Err. nombre medaille par pays")

    def testpaysAvecLePlusDeMedaille(self):
        ep = Epreuve("Women's Street")
        jeu = Jeu(2020, "Tokyo", [])

        ath1 = Athlete("RAYSSA", "Leal", Pays("Brésil", "portugais"), 2020, "Tokyo")
        medaille1 = Medaille("Argent", ep)

        medaille1.attribuer(ath1)
        jeu.ajouterMedaille(medaille1)

        ath2 = Athlete("Romain", "Alicia", Pays("France", "français"), 2020, "Tokyo")
        medaille2 = Medaille("Or", ep)

        medaille2.attribuer(ath2)
        jeu.ajouterMedaille(medaille2)

        ath3 = Athlete("Azerty", "Clara", Pays("France", "français"), 2020, "Tokyo")
        medaille3 = Medaille("Bronze", ep)

        medaille3.attribuer(ath3)
        jeu.ajouterMedaille(medaille3)
        
        self.assertEqual(["France"], jeu.paysAyantLePlusDeMedaille(), "Err. nombre medaille par pays")


if __name__ == '__main__':
    unittest.main()
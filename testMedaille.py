import unittest

from athlete import Athlete
from epreuve import Epreuve
from medaille import Medaille
from pays import Pays


class TestMedaille(unittest.TestCase):
    def testCreationMedaille(self):
        ep = Epreuve("Women's Street")
        ath = Athlete("RAYSSA", "Leal", Pays("Brésil", "portugais"), 2020, "Tokyo")
        medaille = Medaille("Argent", ep, ath)
        self.assertEqual("RAYSSA",medaille.getAthlete().getNom(), "Err. attribution de la medaille")  # add assertion here


if __name__ == '__main__':
    unittest.main()

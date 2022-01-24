import unittest

from src.webcontent.active import ActivateCases
from src.webcontent.reported import ReportedCases
from src.webcontent.vaccines import VaccineDosesPercent, VaccineDoses
from src.saucier.soup import Soup


class TestSoup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._url = "https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx"
        cls.soup = Soup.from_url(cls._url, 'lxml')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_repr(self):
        self.assertEqual(repr(self.soup),
            "Soup(https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx, lxml)")



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


class TestActivateCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._url = "https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx"
        cls.soup = Soup.from_url(cls._url, 'lxml')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_cases_are_integers(self):
        active_cases = ActivateCases(self.soup)
        self.assertIsInstance(active_cases.active, int)
        self.assertIsInstance(active_cases.hospital, int)
        self.assertIsInstance(active_cases.icu, int)
        self.assertIsInstance(active_cases.ventilation, int)

    def test_hospital_less_than_active(self):
        active_cases = ActivateCases(self.soup)
        self.assertLess(active_cases.hospital, active_cases.active)

    def test_icu_less_than_hospital(self):
        active_cases = ActivateCases(self.soup)
        self.assertLess(active_cases.icu, active_cases.hospital)

    def test_ventilation_less_than_icu(self):
        active_cases = ActivateCases(self.soup)
        self.assertLess(active_cases.ventilation, active_cases.icu)

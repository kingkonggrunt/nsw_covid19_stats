import unittest

from src.webcontent.active import ActivateCases
from src.webcontent.reported import ReportedCases
from src.webcontent.vaccines import VaccineDosesPercent, VaccineDoses
from src.saucier.soup import Soup


class TestSoup(unittest.TestCase):
    """Test that the soup class is working"""
    
    @classmethod
    def setUpClass(cls):
        cls._url = "https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx"
        cls.soup = Soup.from_url(cls._url, 'lxml')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_repr(self):
        """Test that the __repr__ method is working"""
        self.assertEqual(repr(self.soup),
            "Soup(https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx, lxml)")


class TestActivateCases(unittest.TestCase):
    """Test Proper Webscraping of Active Cases Stats"""
    @classmethod
    def setUpClass(cls):
        cls._url = "https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx"
        cls.soup = Soup.from_url(cls._url, 'lxml')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_cases_are_integers(self):
        """Test that a number was scraped"""
        
        active_cases = ActivateCases(self.soup)
        self.assertIsInstance(active_cases.active, int)
        self.assertIsInstance(active_cases.hospital, int)
        self.assertIsInstance(active_cases.icu, int)
        self.assertIsInstance(active_cases.ventilation, int)

    def test_hospital_less_than_active(self):
        """Test that hospital cases are less than active (ie. web scraping is looking at the right places)"""
        
        active_cases = ActivateCases(self.soup)
        self.assertLess(active_cases.hospital, active_cases.active)

    def test_icu_less_than_hospital(self):
        """Test that icu cases are less than hospital cases (ie. web scraping is looking at the right places)"""
        
        active_cases = ActivateCases(self.soup)
        self.assertLess(active_cases.icu, active_cases.hospital)

    def test_ventilation_less_than_icu(self):
        """Test that ventilation cases are less than icu cases (ie. web scraping is looking at the right places)"""
        active_cases = ActivateCases(self.soup)
        self.assertLess(active_cases.ventilation, active_cases.icu)


class TestReportedCases(unittest.TestCase):
    """Test Proper Webscraping of Reported Cases"""
    
    @classmethod
    def setUpClass(cls):
        cls._url = "https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx"
        cls.soup = Soup.from_url(cls._url, 'lxml')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_cases_are_integers(self):
        """Test that a number was extracted"""
        
        reported = ReportedCases(self.soup)
        self.assertIsInstance(reported.day, int)
        self.assertIsInstance(reported.week, int)
        self.assertIsInstance(reported.lastweek, int)
        self.assertIsInstance(reported.total, int)

    def test_day_less_than_week(self):
        """"Test that the scraped day value is lower than the week value (ie. to test if the scraping is working correctly)"""
        
        reported = ReportedCases(self.soup)
        self.assertLess(reported.day, reported.week)

    def test_day_week_last_week_less_than_total(self):
        """Test that the scraped day, week, and last week values are less than the total. (ie. to test if the scraping is working correctly)"""
        
        reported = ReportedCases(self.soup)
        self.assertLess(reported.day, reported.total)
        self.assertLess(reported.week, reported.total)
        self.assertLess(reported.lastweek, reported.total)


class TestVaccines(unittest.TestCase):
    """Test proper web scraping of the vaccines stats"""
    
    @classmethod
    def setUpClass(cls):
        cls._url = "https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx"
        cls.soup = Soup.from_url(cls._url, 'lxml')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_vaccines_are_integers(self):
        """Test that a number was extracted"""
        
        vaccines = VaccineDoses(self.soup)
        self.assertIsInstance(vaccines.first_day, int)
        self.assertIsInstance(vaccines.second_day, int)
        self.assertIsInstance(vaccines.third_day, int)
        self.assertIsInstance(vaccines.total_day, int)
        self.assertIsInstance(vaccines.first_total, int)
        self.assertIsInstance(vaccines.second_total, int)
        self.assertIsInstance(vaccines.third_total, int)
        self.assertIsInstance(vaccines.total_total, int)
        self.assertIsInstance(vaccines.total_total_other, int)
        self.assertIsInstance(vaccines.total_doses, int)

    def test_days_less_than_total(self):
        """"Test that day values are less than total (ie. to test if the scraping is working correctly"""
        
        vaccines = VaccineDoses(self.soup)
        self.assertLess(vaccines.first_day, vaccines.first_total)
        self.assertLess(vaccines.second_day, vaccines.second_total)
        self.assertLess(vaccines.third_day, vaccines.third_total)
        self.assertLess(vaccines.total_day, vaccines.total_total)

    def test_first_second_third_totals_less_than_each_other(self):
        """"Test that first, second, third doses totals are greater than each other (ie. to test if the scraping is working correctly"""
        
        vaccines = VaccineDoses(self.soup)
        self.assertLess(vaccines.third_total, vaccines.second_total)
        self.assertLess(vaccines.second_total, vaccines.first_total)
        self.assertLess(vaccines.first_total, vaccines.total_total)

    def test_total_total_and_total_total_other_equals_total_doses(self):
        """"Test that the total_total (nsw), total_total_other (non nsw health), and total (both) totals are equal (ie. to test if the scraping is working correctly"""
        
        vaccines = VaccineDoses(self.soup)
        self.assertEqual(vaccines.total_total + vaccines.total_total_other,
            vaccines.total_doses)


class TestVaccinesPercent(unittest.TestCase):
    """Test Vaccine Percentage Stats"""
    
    @classmethod
    def setUpClass(cls):
        cls._url = "https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx"
        cls.soup = Soup.from_url(cls._url, 'lxml')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_properties_are_str(self):
        """Test that something was extracted (ie. that the web scraper was looking at the right places)"""
        
        vaccines_percent = VaccineDosesPercent(self.soup)
        self.assertIsInstance(vaccines_percent.first_16_above, str)
        self.assertIsInstance(vaccines_percent.first_12_to_15, str)
        self.assertIsInstance(vaccines_percent.first_5_to_11, str)
        self.assertIsInstance(vaccines_percent.second_16_above, str)
        self.assertIsInstance(vaccines_percent.second_12_to_15, str)
        self.assertIsInstance(vaccines_percent.second_5_to_11, str)
        self.assertIsInstance(vaccines_percent.third_16_above, str)
        self.assertIsInstance(vaccines_percent.third_12_to_15, str)
        self.assertIsInstance(vaccines_percent.third_5_to_11, str)

"""updater.py
    file containing the updater class for the API

"""
import redis
from ..redis.redis import RedisDictionary
from ..saucier.soup import Soup
from ..webcontent import active, reported, vaccines


class RedisUpdater():  #TODO: ? better name (too misleading)
    """Updater for the API's Redis Database

    Parameters
    ----------
    rdict : RedisDictionary
        An instance of a RedisDictionary
    soup : Soup
        An instance of a Soup class

    Attributes
    ----------
    rdict
    soup

    """
    def __init__(self, rdict: RedisDictionary, soup: Soup):
        self.rdict = rdict
        self.soup = soup

    def _update_active(self):
        """Updates the active stats"""
        _active = active.ActivateCases(self.soup)

        self.rdict.multi_set({
            "active": _active.active,
            "hospital": _active.hospital,
            "icu": _active.icu,
            "ventilation": _active.ventilation,
        })

    def _update_reported(self):
        """Updates the reported stats"""
        _reported = reported.ReportedCases(self.soup)

        self.rdict.multi_set({
            "reported_day": _reported.day,
            "reported_week": _reported.week,
            "reported_lastweek": _reported.lastweek,
            "reported_total": _reported.total,
        })

    def _update_vaccines(self):
        """Updates the Vaccine stats"""
        _vaccines_percent = vaccines.VaccineDosesPercent(self.soup)

        self.rdict.multi_set({
            "first_16_above": _vaccines_percent.first_16_above,
            "first_5_to_11": _vaccines_percent.first_5_to_11,
            "first_12_to_15": _vaccines_percent.first_12_to_15,
            "second_16_above": _vaccines_percent.second_16_above,
            "second_5_to_11": _vaccines_percent.second_5_to_11,
            "second_12_to_15": _vaccines_percent.second_12_to_15,
            "third_16_above": _vaccines_percent.third_16_above,
            "third_5_to_11": _vaccines_percent.third_5_to_11,
            "third_12_to_15": _vaccines_percent.third_12_to_15,
        })

    def update(self):
        """Updates the redis db"""
        self._update_active()
        self._update_reported()
        self._update_vaccines()

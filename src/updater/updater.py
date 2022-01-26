import redis
from ..redis.redis import RedisDictionary
from ..saucier.soup import Soup
from ..webcontent import active, reported, vaccines


class RedisUpdater():
    def __init__(self, rdict: RedisDictionary, soup: Soup):
        self.rdict = rdict
        self.soup = soup

    def _update_active(self):
        _active = active.ActivateCases(self.soup)

        self.rdict.multi_set({
            "active": _active.active,
            "hospital": _active.hospital,
            "icu": _active.icu,
            "ventilation": _active.ventilation,
        })

    def _update_reported(self):
        _reported = reported.ReportedCases(self.soup)

        self.rdict.multi_set({
            "reported_day": _reported.day,
            "reported_week": _reported.week,
            "reported_lastweek": _reported.lastweek,
            "reported_total": _reported.total,
        })

    def _update_vaccines(self):
        _vaccines = vaccines.VaccineDoses(self.soup)
        _vaccines_percent = vaccines.VaccineDosesPercent(self.soup)

        self.rdict.multi_set({
            "daily_nsw_first": _vaccines.first_day,
            "daily_nsw_second": _vaccines.second_day,
            "daily_nsw_third": _vaccines.third_day,
            "daily_nsw_total": _vaccines.total_day,
            "total_nsw_first": _vaccines.first_total,
            "total_nsw_second": _vaccines.second_total,
            "total_nsw_third": _vaccines.third_total,
            "total_nsw_total": _vaccines.total_total,
            "total_nsw": _vaccines.total_total,
            "total_other": _vaccines.total_total_other,
            "total": _vaccines.total_doses,
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
        self._update_active()
        self._update_reported()
        self._update_vaccines()
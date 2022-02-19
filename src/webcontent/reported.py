from ..saucier.soup import Soup
from ..saucier.utensils import *  #i know what i'm doing here

class ReportedCases():
    """Reported Covid Cases in NSW

    Parameters
    ----------
    Soup : Soup
        A Soup Class instantiated with the `from_url` class

    Attributes
    ----------
    soup : Soup
        A Soup Class
    _attr : dict
        Attributes for the Reported Cases Table
    _attr_col : dict
        Attributes for the column containing values in the Reported Cases Table
    day : int
        no. of cases in the past 24 hours
    week : int
        no. of cases in the past week
    lastweek : int
        no. of cases in the past week before last (14-8 days ago)
    total : int
        no. of cases in total

    """
    _attr = {"class": "moh-rteTable-6 cases"}
    _attr_col = {"class": "moh-rteTableOddCol-6"}

    def __init__(self, Soup: Soup):
        self.soup = Soup
        self._tag = self.soup.find(attrs=self._attr)

        self.day = self._tag
        self.week = self._tag
        self.lastweek = self._tag
        self.total = self._tag

    """Property: day
        no. of reported cases in the past 24 hours

    Variables
    ---------
    _attr_row: dict
        attributes for the `day` row
    """
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, tag):
        _attr_row = {"class": "moh-rteTableOddRow-6"}

        item = grab_table_item(tag, _attr_row, self._attr_col, None, 2)
        self._day = int(item.text.replace(",", ''))

    """Property: week
        no. of reported cases in the past week

    Variables
    ---------
    _attr_row: dict
        attributes for the `week` row
    """
    @property
    def week(self):
        return self._week

    @week.setter
    def week(self, tag):
        _attr_row = {"class": "moh-rteTableEvenRow-6"}

        item = grab_table_item(tag, _attr_row, self._attr_col, None, 2)
        self._week = int(item.text.replace(",", ''))

    """Property: lastweek
        no. of cases
    Variables
    ---------
    _attr_row: dict
        no. of cases in the past week before last (14-8 days ago)

    Unlike property `week`, `lastweek` is found using a list search

    """
    @property
    def lastweek(self):
        return self._lastweek

    @lastweek.setter
    def lastweek(self, tag):
        _attr_row = {"class": "moh-rteTableOddRow-6"}

        item = grab_table_item(tag, _attr_row, self._attr_col, 1, 2)
        self._lastweek = int(item.text.replace(",", ''))

    """Property: total
        no. of cases total

    Variables
    ---------
    _attr_row: dict
        attributes for the `total` row (footer)
    _attr_col: dict
        attributes for the `total` value

    """
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, tag):
        _attr_row = {"class": "moh-rteTableFooterRow-6"}
        _attr_col = {"class": "moh-rteTableFooterOddCol-6"}

        item = grab_table_item(tag, _attr_row, _attr_col)
        self._total = int(item.text.replace(",", ''))

from ..saucier.soup import Soup
from ..saucier.utensils import grab_table_item

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

    @property
    def day(self):
        """Total amount of cases in the past 24 hours."""
        return self._day

    @day.setter
    def day(self, tag):
        """Total amount of cases in the past 24 hours."""
        row_class = "moh-rteTableOddRow-6"
        col_class = "moh-rteTableOddCol-6"

        item = grab_table_item(tag, {"class": row_class}, {"class": col_class}, 0, 2)
        self._day = int(item.text.replace(",", ''))

    @property
    def week(self):
        """Total amount of cases in the past week"""
        return self._week

    @week.setter
    def week(self, tag):
        """Total amount of cases in the past week"""
        row_class = "moh-rteTableEvenRow-6"
        col_class = "moh-rteTableOddCol-6"

        item = grab_table_item(tag, {"class": row_class}, {"class": col_class}, 0, 2)
        self._week = int(item.text.replace(",", ''))

    @property
    def lastweek(self):
        """Total amount of cases in the week before last week"""
        return self._lastweek

    @lastweek.setter
    def lastweek(self, tag):
        """Total amount of cases in the week before last week"""
        row_class = "moh-rteTableOddRow-6"
        col_class = "moh-rteTableOddCol-6"

        item = grab_table_item(tag, {"class": row_class}, {"class": col_class}, 1, 2)
        self._lastweek = int(item.text.replace(",", ''))

    @property
    def total(self):
        """Total amount of covid cases"""
        return self._total

    @total.setter
    def total(self, tag):
        """Finds the total amount of covid cases since the beginning of the pandemic"""
        row_class = "moh-rteTableEvenRow-6"
        col_class = "moh-rteTableEvenCol-6"

        item = grab_table_item(tag, {"class": row_class}, {"class": col_class}, 1, 3)
        self._total = int(item.text.replace(",", ''))

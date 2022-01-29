"""vaccines.py
    contains the VaccineDoses and VaccineDosesPercent classes
"""
from ..saucier.soup import Soup
from ..saucier.utensils import *  #i know what i'm doing there


class VaccineDosesPercent():
    _attr = {"class": "vax-update moh-rteTable-6"}
    _table_index = 0

    _attr_row = {
        "first" : {"class": "moh-rteTableOddRow-6"},
        "second" : {"class": "moh-rteTableEvenRow-6"},
        "third" : {"class": "moh-rteTableOddRow-6"}
    }
    _attr_col = {
        "16_above" : {"class": "moh-rteTableOddCol-6"},
        "12_to_15" : {"class": "moh-rteTableEvenCol-6"},
        "5_to_11" : {"class": "moh-rteTableOddCol-6"}
    }
    _index_rows = {
        "first" : 0,
        "second" : 0,
        "third" : 1
    }
    _index_cols = {
        "16_above" : 0,
        "12_to_15" : 1,
        "5_to_11" : 1
    }

    def __init__(self, Soup: Soup):
        """VaccineDosesPercent
            Vaccine Doses Population Numbers

        Parameters
        ----------
        Soup : Soup
            A Soup Class instantiated with the `from_url` class

        Attributes
        -------
        self._attr, _attr_row, _attr_col, _index_rows, _index_cols : dict
            dictionaries used to locate the relavent html element
        self._tag
            the "vax-update calloutbox" tag

        Properties
        ----------
        first_16_above
        first_5_to_11
        first_12_to_15
        second_16_above
        second_5_to_11
        second_12_to_15
        third_16_above
        third_5_to_11
        third_12_to_15

        """
        self.soup = Soup
        self._tag = self.soup.find_all(attrs=self._attr)[self._table_index]

        self.first_16_above = self._tag
        self.first_5_to_11  = self._tag
        self.first_12_to_15 = self._tag

        self.second_16_above = self._tag
        self.second_5_to_11  = self._tag
        self.second_12_to_15 = self._tag

        self.third_16_above = self._tag
        self.third_5_to_11  = self._tag
        self.third_12_to_15 = self._tag

    """Property: first_16_above
        no. of first doses given to people 16 and above
    """
    @property
    def first_16_above(self):
        return self._first_16_above

    @first_16_above.setter
    def first_16_above(self, tag):

        item = grab_table_item(tag, self._attr_row["first"], self._attr_col["16_above"],
            self._index_rows["first"], self._index_cols["16_above"])
        self._first_16_above = item.text

    """Property: first_5_to_11
        no. of first doses given to people between 5 and 11
    """
    @property
    def first_5_to_11(self):
        return self._first_5_to_11

    @first_5_to_11.setter
    def first_5_to_11(self, tag):

        item = grab_table_item(tag, self._attr_row["first"], self._attr_col["5_to_11"],
            self._index_rows["first"], self._index_cols["5_to_11"])
        self._first_5_to_11 = item.text

    """Property: first_12_to_15
        no. of first doses given to people between 12 and 15
    """
    @property
    def first_12_to_15(self):
        return self._first_12_to_15

    @first_12_to_15.setter
    def first_12_to_15(self, tag):

        item = grab_table_item(tag, self._attr_row["first"], self._attr_col["12_to_15"],
            self._index_rows["first"], self._index_cols["12_to_15"])
        self._first_12_to_15 = item.text

    """Property: second_16_above
        no. of second doses given to people 16 and above
    """
    @property
    def second_16_above(self):
        return self._second_16_above

    @second_16_above.setter
    def second_16_above(self, tag):

        item = grab_table_item(tag, self._attr_row["second"], self._attr_col["16_above"],
            self._index_rows["second"], self._index_cols["16_above"])
        self._second_16_above = item.text

    """Property: second_5_to_11
        no. of second doses given to people between 5 and 11
    """
    @property
    def second_5_to_11(self):
        return self._second_5_to_11

    @second_5_to_11.setter
    def second_5_to_11(self, tag):

        item = grab_table_item(tag, self._attr_row["second"], self._attr_col["5_to_11"],
            self._index_rows["second"], self._index_cols["5_to_11"])
        self._second_5_to_11 = item.text

    """Property: second_12_to_15
        no. of second doses given to people between 12 and 15
    """
    @property
    def second_12_to_15(self):
        return self._second_12_to_15

    @second_12_to_15.setter
    def second_12_to_15(self, tag):

        item = grab_table_item(tag, self._attr_row["second"], self._attr_col["12_to_15"],
            self._index_rows["second"], self._index_cols["12_to_15"])
        self._second_12_to_15 = item.text

    """Property: third_16_above
        no. of third doses given to people 16 and above
    """
    @property
    def third_16_above(self):
        return self._third_16_above

    @third_16_above.setter
    def third_16_above(self, tag):

        item = grab_table_item(tag, self._attr_row["third"], self._attr_col["16_above"],
            self._index_rows["third"], self._index_cols["16_above"])
        self._third_16_above = item.text

    """Property: third_5_to_11
        no. of third doses given to people between 5 and 11
    """
    @property
    def third_5_to_11(self):
        return self._third_5_to_11

    @third_5_to_11.setter
    def third_5_to_11(self, tag):

        item = grab_table_item(tag, self._attr_row["third"], self._attr_col["5_to_11"],
            self._index_rows["third"], self._index_cols["5_to_11"])
        self._third_5_to_11 = item.text

    """Property: third_12_to_15
        no. of third doses given to people between 12 and 15
    """
    @property
    def third_12_to_15(self):
        return self._third_12_to_15

    @third_12_to_15.setter
    def third_12_to_15(self, tag):

        item = grab_table_item(tag, self._attr_row["third"], self._attr_col["12_to_15"],
            self._index_rows["third"], self._index_cols["12_to_15"])
        self._third_12_to_15 = item.text


class VaccineDoses():
    _attr = {"class": "vax-update moh-rteTable-6"}
    _table_index = 1
    _table_index_other = 2

    _attr_row = {
        "first": {"class": "moh-rteTableOddRow-6"},
        "second": {"class": "moh-rteTableEvenRow-6"},
        "third": {"class": "moh-rteTableOddRow-6"},
        "total": {"class": "moh-rteTableFooterRow-6"}
    }
    _attr_cols = {
        "day": {"class": "moh-rteTableOddCol-6"},
        "total": {"class": "moh-rteTableEvenCol-6"},
        "total_day": {"class": "moh-rteTableFooterOddCol-6"},
        "total_total": {"class": "moh-rteTableFooterEvenCol-6"},
    }
    _index_rows = {
        "first": 0,
        "second": 0,
        "third": 1,
        "total": None
    }
    _index_cols = {
        "day": 0,
        "total": 1,
        "total_day": 0,
        "total_total": 1,
    }

    def __init__(self, Soup: Soup):
        """VaccineDoses
            Vaccine Doses Numbers

        Parameters
        ----------
        Soup : Soup
            A Soup Class instantiated with the `from_url` class

        Attributes
        -------
        self._attr, _attr_row, _attr_col, _index_rows, _index_cols : dict
            dictionaries used to locate the relavent html element
        self._tag
            the "vax-update calloutbox" tag

        Properties
        ----------
        first_day
        second_day
        third_day
        total_day
        first_total
        second_total
        third_total
        total_total
        total_total_other
        total_doses

        """
        self.soup = Soup
        self._tag = self.soup.find_all(attrs=self._attr)[self._table_index]
        self._tag_other = self.soup.find_all(attrs=self._attr)[self._table_index_other]

        self.first_day = self._tag
        self.second_day = self._tag
        self.third_day = self._tag
        self.total_day = self._tag

        self.first_total = self._tag
        self.second_total = self._tag
        self.third_total = self._tag
        self.total_total = self._tag

        self.total_total_other = self._tag_other
        self.total_doses = self._tag_other

    """Property: first_day
        no. of first doses in the past 24 hours
    """
    @property
    def first_day(self):
        return self._first_day

    @first_day.setter
    def first_day(self, tag):

        item = grab_table_item(tag, self._attr_row["first"], self._attr_cols["day"],
            self._index_rows["first"], self._index_cols["day"])
        self._first_day = int(item.text.replace(",", ''))

    """Property: second_day
        no. of second doses in the past 24 hours
    """
    @property
    def second_day(self):
        return self._second_day

    @second_day.setter
    def second_day(self, tag):

        item = grab_table_item(tag, self._attr_row["second"], self._attr_cols["day"],
            self._index_rows["second"], self._index_cols["day"])
        self._second_day = int(item.text.replace(",", ''))

    """Property: third_day
        no. of third doses in the past 24 hours
    """
    @property
    def third_day(self):
        return self._third_day

    @third_day.setter
    def third_day(self, tag):

        item = grab_table_item(tag, self._attr_row["third"], self._attr_cols["day"],
            self._index_rows["third"], self._index_cols["day"])
        self._third_day = int(item.text.replace(",", ''))

    """Property: third_12_to_15
        no. of third doses given to people between 12 and 15
    """
    @property
    def total_day(self):
        return self._total_day

    @total_day.setter
    def total_day(self, tag):

        item = grab_table_item(tag, self._attr_row["total"], self._attr_cols["total_day"],
            self._index_rows["total"], self._index_cols["total_day"])
        self._total_day = int(item.text.replace(",", ''))

    """Property: first_total
        no. of first doses in total
    """
    @property
    def first_total(self):
        return self._first_total

    @first_total.setter
    def first_total(self, tag):

        item = grab_table_item(tag, self._attr_row["first"], self._attr_cols["total"],
            self._index_rows["first"], self._index_cols["total"])
        self._first_total = int(item.text.replace(",", ''))

    """Property: second_total
        no. of second doses in total
    """
    @property
    def second_total(self):
        return self._second_total

    @second_total.setter
    def second_total(self, tag):

        item = grab_table_item(tag, self._attr_row["second"], self._attr_cols["total"],
            self._index_rows["second"], self._index_cols["total"])
        self._second_total = int(item.text.replace(",", ''))

    """Property: third_total
        no. of third doses in total
    """
    @property
    def third_total(self):
        return self._third_total

    @third_total.setter
    def third_total(self, tag):

        item = grab_table_item(tag, self._attr_row["third"], self._attr_cols["total"],
            self._index_rows["third"], self._index_cols["total"])
        self._third_total = int(item.text.replace(",", ''))

    """Property: total_total
        no. of all doses given in total in the NSW Health Covid Vaccination network
    """
    @property
    def total_total(self):
        return self._total_total

    @total_total.setter
    def total_total(self, tag):

        item = grab_table_item(tag, self._attr_row["total"], self._attr_cols["total_total"],
            self._index_rows["total"], self._index_cols["total_total"])
        self._total_total = int(item.text.replace(",", ''))

    """Property: total_total_other
        no. of all doses given in total outside of the NSW Health Covid Vaccination network
    """
    @property
    def total_total_other(self):
        return self._total_total_other  # TODO: ? is a better variable name better?

    @total_total_other.setter
    def total_total_other(self, tag):
        item = grab_table_item(tag, {"class": "moh-rteTableEvenRow-6"}, {"class": "moh-rteTableOddCol-6"})
        self._total_total_other = int(item.text.replace(",", ''))

    """Property: total_doses
        no. of all doses given in NSW
    """
    @property
    def total_doses(self):
        return self._total_doses

    @total_doses.setter
    def total_doses(self, tag):
        item = grab_table_item(tag, {"class": "moh-rteTableFooterRow-6"}, {"class": "moh-rteTableFooterOddCol-6"})
        self._total_doses = int(item.text.replace(",", ''))

from ..saucier.soup import Soup

def return_li_item_with_text_search(tag, text):
    """Finds a single <li> item based on text content

    Parameters
    ----------
    tag : Tag
        an iteratable parent element: <ol>, <ul>, or <menu>
    text : str
        search text

    Returns
    -------
    Tag
        <li> item

    """
    for item in tag.find_all("li"):
        if text in item.text:
            return item


class ActivateCases():
    _attr = {"class": "active-cases calloutbox"}

    def __init__(self, Soup: Soup):
        """Active Covid Cases in NSW

        Parameters
        ----------
        Soup : Soup
            A Soup Class instantiated with the `from_url` class

        Attributes
        ----------
        self._attr : dict
            attrs to find the "active-cases calloutbox"
        self._tag
            the "active-cases calloutbox" tag

        Properties
        ----------
        active
            no. of active covid cases
        hopsital
            no. of active covid hospitalisations
        icu
            no. of active icu cases
        ventilation
            no. of active cases on ventilation

        """
        self.soup = Soup
        self._tag = self.soup.find(attrs=self._attr)

        self.active = self._tag
        self.hospital = self._tag
        self.icu = self._tag
        self.ventilation = self._tag

    """
    Property: ventilation
        no. of active cases on ventilation
    """
    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, tag):
        item = return_li_item_with_text_search(tag, "Active cases")
        self._active = int(item.text.replace("Active cases", '').replace(",", ''))

    """
    Property: hospital
        no. of active covid hospitalisations
    """
    @property
    def hospital(self):
        return self._hospital

    @hospital.setter
    def hospital(self, tag):
        item = return_li_item_with_text_search(tag, "Admitted to hospital")
        self._hospital = int(item.text.replace("Admitted to hospital", '').replace(",", ''))

    """
    Property: icu
        no. of active icu cases
    """
    @property
    def icu(self):
        return self._icu

    @icu.setter
    def icu(self, tag):
        item = return_li_item_with_text_search(tag, "In intensive care")
        self._icu = int(item.text.replace("In intensive care", '').replace(",", ''))

    """
    Property: ventilation
        no. of active cases on ventilation
    """
    @property
    def ventilation(self):
        return self._ventilation

    @ventilation.setter
    def ventilation(self, tag):
        item = return_li_item_with_text_search(tag, "Requiring ventilation")
        self._ventilation = int(item.text.replace("Requiring ventilation", '').replace(",", ''))

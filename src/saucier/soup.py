import requests
from bs4 import BeautifulSoup
import lxml

class Soup(BeautifulSoup):
    """A BeautifulSoup Class"""
    @classmethod
    def from_url(cls, url, features):
        """Create Soup from url

        Parameters
        ----------
        url : str
            website url
        features : str
            Desirable features of the parser to be used

        Returns
        -------
        Soup
            A BeautifulSoup Class

        """
        url_data = requests.get(url)
        cls._url = url
        cls._features = features
        return cls(url_data.content, features)

    def __repr__(self):
        return f"Soup({self._url}, {self._features})"

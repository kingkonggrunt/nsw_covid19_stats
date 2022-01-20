from src.webcontent.active import ActivateCases
from src.saucier.soup import Soup



def main():
    url = "https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx"
    soup = Soup.from_url(url, 'lxml')

    active_cases = ActivateCases(soup)
    print(active_cases.active)
    print(active_cases.hospital)
    print(active_cases.icu)
    print(active_cases.ventilation)


    return

if __name__ == "__main__":
    main()

from src.webcontent.active import ActivateCases
from src.saucier.soup import Soup
from src.redis.redis import RedisDictionary

import redis



def main():
    url = "https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx"
    soup = Soup.from_url(url, 'lxml')

    active_cases = ActivateCases(soup)
    print(active_cases.active)
    print(active_cases.hospital)
    print(active_cases.icu)
    print(active_cases.ventilation)



    rdict = RedisDictionary(redis.Redis, db=2)
    print(repr(rdict))
    # rdict["active"] = active_cases.active
    # rdict["hospital"] = active_cases.hospital
    # rdict["icu"] = active_cases.icu
    # rdict["ventilation"] = active_cases.ventilation
    #
    # print(rdict["ventilation"])

    return

if __name__ == "__main__":
    main()

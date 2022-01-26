import time
import redis
from src.redis.redis import RedisDictionary
from src.saucier.soup import Soup
from src.updater.updater import RedisUpdater


rdict = RedisDictionary(redis.Redis, db=2)

def main():
    while True:
        url = "https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx"
        soup = Soup.from_url(url, 'lxml')
        updater = RedisUpdater(rdict, soup)
        updater.update()
        time.sleep(3*60*60)


if __name__ == '__main__':
    main()
# NSW COVID 19 STATS

An API written with the `FastAPI` framework that provides the NSW Covid Stats found on [NSW COVID 19 Stats Page](https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx) - Active Cases, Reported Cases, and Vaccine Numbers.

The numbers on the page are webscraped using `BeautifulSoup4` and saved to a `Redis` database. This allows the API to maintain performance and decouples the updating of information with the API.  

Currently you can interact with the API @ `dcong.page/covid-stats` (HTTPS)

#### Installation and Setup (Tested on Ubuntu 20.04)
- Ensure you have a running redis database on your system on port `6379`
1. Clone this repo `git clone https://github.com/kingkonggrunt/nsw_covid19_stats.git`
2. Enter the directory `cd nsw_covid19_stats`
3. Create and activate a venv `python3 -m venv venv` `. venv/bin/activate`
4. Install packages `pip3 install -r requirements.txt`

- Launch the API using `uvicorn api:app --reload` on your localhost in devmode. Use `uvicorn api:app --host 0.0.0.0 --port 3400` to launch the API exposed to the internet - accessible by your IP address.
- Launch the updater using `python3 updater.py`. The updater just updates values every 3 hours.

#### Next Steps
- HTTPS
- Custom Domain Name
- Updater Tweaks

*Author:* *Duc Cong Duong*

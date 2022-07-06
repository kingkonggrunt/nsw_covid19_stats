"""api.py
    Main file to run the api

If using your own redis configuration, consider that the current db value `2`,
may need to be modified. RedisDictionary only allows changing of the db connection number.
TODO: **kwargs for redisdictionary

"""

from fastapi import FastAPI

import redis
from src.redishelper.redishelper import RedisDictionary


app = FastAPI()
r = RedisDictionary(redis.Redis, db=2)



class NGINXConfig():
    """Custom Class for configuring the api for NGINX deployment"""
    uri = "/covid-stats"  # base uri where api with deployed example.com/<uri>
    ## prefix parameter in include router doesn't worka

@app.get(f"{NGINXConfig.uri}/")
def root():
    "List avaible routes for the end user"
    return {
        "Welcome": "Routes are listed below",
        "/": "This Route",
        "/active": {
            " ": "no. of active, hospital, icu and ventilation cases",
            "/cases": "no. of active cases",
            "/hospital": "no. of hospital cases",
            "/icu" : "no. of icu cases",
            "/ventilation": "no. of ventilation cases"
        },
        "/reported": {
            " ": "no. reported cases in for the last day, week, lastweek, and total cases",
            "/day": "no. of reported cases in the last 24 hours",
            "/week": "no. of reported cases in the last 7 days",
            "/lastweek": "no. of reported cases in the last 8-14 days",
            "/total": "no. of total reported cases"
        },
        "/vaccines": {
            " ": "vaccine population distrubition stats",
            "/population": "vaccine population distrubition stats"
        }
    }


# ===== Active Cases
@app.get(f"{NGINXConfig.uri}/active")
def active():
    """returns the active no. of `active`, `hospital`, `icu` and `ventilation` cases"""
    return {
        "active": r["active"],
        "hospital": r["hospital"],
        "icu": r["icu"],
        "ventilation": r["ventilation"],
    }

@app.get(f"{NGINXConfig.uri}/active/cases")
def active_cases():
    """returns the active no. of cases"""
    return {"amount": r["active"]}

@app.get(f"{NGINXConfig.uri}/active/hospital")
def active_hospital():
    """returns the active no. of hospital cases"""
    return {"amount": r["hospital"]}

@app.get(f"{NGINXConfig.uri}/active/icu")
def active_icu():
    """returns the active no. of icu cases"""
    return {"amount": r["icu"]}

@app.get(f"{NGINXConfig.uri}/active/ventilation")
def active_ventilation():
    """returns the active no. of ventilation cases"""
    return {"amount": r["ventilation"]}



# ===== Reported

@app.get(f"{NGINXConfig.uri}/reported")
def reported():
    """returns the reported no. of cases for the last `day`, `week`, `lastweek`, and `total` cases"""
    return {
        "day": r["reported_day"],
        "week": r["reported_week"],
        "lastweek": r["reported_lastweek"],
        "total": r["reported_total"],
    }
@app.get(f"{NGINXConfig.uri}/reported/day")
def reported_day():
    """returns the reported no. of cases for the past 24 hours (day)"""
    return {"amount": r["reported_day"]}

@app.get(f"{NGINXConfig.uri}/reported/week")
def reported_week():
    """returns the reported no. of cases for the past 7 days"""
    return {"amount": r["reported_week"]}

@app.get(f"{NGINXConfig.uri}/reported/lastweek")
def reported_lastweek():
    """returns the reported no. of cases for the past 8-14 days"""
    return {"amount": r["reported_lastweek"]}

@app.get(f"{NGINXConfig.uri}/reported/total")
def reported_total():
    """returns the total reported no. of cases"""
    return {"amount": r["reported_total"]}



# ===== Vaccines

@app.get(f"{NGINXConfig.uri}/vaccines")
def vaccines():
    """return both the vaccine doses and vaccine population distrubition stats"""
    return {
        "population": {
            "16_above": {
                "first": r["first_16_above"],
                "second": r["second_16_above"],
                "third": r["third_16_above"],
            },
            "12_to_15": {
                "first": r["first_12_to_15"],
                "second": r["second_12_to_15"],
                "third": r["third_12_to_15"],
            },
            "5_to_11": {
                "first": r["first_5_to_11"],
                "second": r["second_5_to_11"],
                "third": r["third_5_to_11"],
            },
        }

    }

@app.get(f"{NGINXConfig.uri}/vaccines/population")
def vaccines_population():
    "return the vaccine population distrubition stats"
    return {
        "population": {
            "16_above": {
                "first": r["first_16_above"],
                "second": r["second_16_above"],
                "third": r["third_16_above"],
            },
            "12_to_15": {
                "first": r["first_12_to_15"],
                "second": r["second_12_to_15"],
                "third": r["third_12_to_15"],
            },
            "5_to_11": {
                "first": r["first_5_to_11"],
                "second": r["second_5_to_11"],
                "third": r["third_5_to_11"],
            },
        }
    }

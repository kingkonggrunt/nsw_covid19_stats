"""api.py
    Main file to run the api

If using your own redis configuration, consider that the current db value `2`,
may need to be modified. RedisDictionary only allows changing of the db connection number.
TODO: **kwargs for redisdictionary

"""

from fastapi import FastAPI

import redis
from src.redis.redis import RedisDictionary


app = FastAPI()
r = RedisDictionary(redis.Redis, db=2)


@app.get("/")
def root():
    return {"message": "Hello World"}


"""Active Cases

Routes
------
/active
    returns the active no. of `active`, `hospital`, `icu` and `ventilation`
    cases

/active/cases
    returns the active no. of cases

/active/hospital
    returns the active no. of hospital cases

/active/icu
    returns the active no. of icu cases

/active/ventilation
    returns the active no. of ventilation cases

"""
@app.get("/active")
def active():
    return {
        "active": r["active"],
        "hospital": r["hospital"],
        "icu": r["icu"],
        "ventilation": r["ventilation"],
    }

@app.get("/active/cases")
def active_cases():
    return {"amount": r["active"]}

@app.get("/active/hospital")
def active_hospital():
    return {"amount": r["hospital"]}

@app.get("/active/icu")
def active_icu():
    return {"amount": r["icu"]}

@app.get("/active/ventilation")
def active_ventilation():
    return {"amount": r["ventilation"]}


"""Reported Cases

Routes
------
/reported
    returns the reported no. of cases for the last `day`, `week`, `lastweek`,
    and `total` cases

/reported/day
    returns the reported no. of cases for the past 24 hours (day)

/reported/week
    returns the reported no. of cases for the past 7 days

/reported/lastweek
    returns the reported no. of cases for the past 8-14 days

/reported/total
    returns the total reported no. of cases
"""
@app.get("/reported")
def reported():
    return {
        "day": r["reported_day"],
        "week": r["reported_week"],
        "lastweek": r["reported_lastweek"],
        "total": r["reported_total"],
    }

@app.get("/reported/day")
def reported_day():
    return {"amount": r["reported_day"]}

@app.get("/reported/week")
def reported_week():
    return {"amount": r["reported_week"]}

@app.get("/reported/lastweek")
def reported_lastweek():
    return {"amount": r["reported_lastweek"]}

@app.get("/reported/total")
def reported_total():
    return {"amount": r["reported_total"]}


"""Vaccines

Routes
------
/vaccines
    return both the vaccine doses and vaccine population distrubition stats

/vaccines/population
    return the vaccine population distrubition stats

/vaccines/doses
    return the vaccine doses stats
"""
@app.get("/vaccines")
def vaccines():
    return {
        "doses": {
            "daily": {
                "first": r["daily_nsw_first"],
                "second": r["daily_nsw_second"],
                "third": r["daily_nsw_third"],
                "total": r["daily_nsw_total"],
            },
            "all": {
                "first": r["total_nsw_first"],
                "second": r["total_nsw_second"],
                "third": r["total_nsw_third"],
                "all": r["total_nsw_total"],
                "nsw": r["total_nsw"],
                "other": r["total_other"],
                "total": r["total"],
            }
        },
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

@app.get("/vaccines/population")
def vaccines_population():
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

@app.get("/vaccines/doses")
def vaccines_doses():
    return {
        "doses": {
            "daily": {
                "first": r["daily_nsw_first"],
                "second": r["daily_nsw_second"],
                "third": r["daily_nsw_third"],
                "total": r["daily_nsw_total"],
            },
            "all": {
                "first": r["total_nsw_first"],
                "second": r["total_nsw_second"],
                "third": r["total_nsw_third"],
                "all": r["total_nsw_total"],
                "nsw": r["total_nsw"],
                "other": r["total_other"],
                "total": r["total"],
            }
        }
    }

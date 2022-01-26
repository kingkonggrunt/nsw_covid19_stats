from fastapi import FastAPI
from src.api import routes

import redis
from src.redis.redis import RedisDictionary


app = FastAPI()
r = RedisDictionary(redis.Redis, db=2)
#
@app.get("/")
def root():
    return {"message": "Hello World"}
# @app.get("/home")


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


#
# @app.get("/active/active")
# active_cases_active
#
# @app.get("/active/hospital")
# active_cases_hospital
#
# @app.get("/active/icu")
# active_cases_icu
#
# @app.get("/active/hospital")
# active_cases_ventilation

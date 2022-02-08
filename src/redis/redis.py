"""redis.py
    contains classes that interact with Redis for the API
"""
import redis


class RedisDictionary():
    def __init__(self, r: redis.Redis, db):
        """RedisDictionary
            A redis connnection that behaves like a Python Dictionary (by design)

        rdict = RedisDictionary(db=1)
        ridct["key"] = "value"
        rdict["key"]
        >>> "value"

        Parameters
        ----------
        r : redis.Redis
            An uninstanced Redis Class
        db : int
            database number for the redis connection

        """
        self.db = db
        self.r = r(db=self.db)

    def __getitem__(self, key):
        return self.r.get(key).decode('utf-8')

    def __setitem__(self, key, value):
        self.r.set(key, value)

    def __repr__(self):
        return f"RedisDictionary(redis.Redis, db={self.db})"

    def multi_set(self, dict):
        """multi_set
            uses redis' multi set ability to set multiple key:value pairings at once

        Parameters
        ----------
        dict : dict
            Dictionary of key:value pairings

        """
        self.r.mset(dict)

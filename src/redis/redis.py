import redis


class RedisDictionary():
    def __init__(self, r: redis.Redis, db):
        self.db = db
        self.r = r(db=self.db)

    def __getitem__(self, key):
        return self.r.get(key).decode('utf-8')

    def __setitem__(self, key, value):
        self.r.set(key, value)

    def __repr__(self):
        return f"RedisDictionary(redis.Redis, db={self.db})"

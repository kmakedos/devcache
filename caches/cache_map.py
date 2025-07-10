class Cache:
    def __init__(self, size):
        self.cache = {}

    def get(self, key):
        if key in self.cache.keys():
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        self.cache[key] = value


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return 
            bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return
 
class MyHashMap(object):
    def __init__(self):
        self.map=[-1] *(10001)
    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map[key]

    def remove(self, key):
        self.map[key] = -1
 
    
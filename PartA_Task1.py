#Task 1

#implementing hash table for finding a post by unique datetime value

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size


    def _hash(self, key):
        return hash(key) % self.size


#Task 1

#implementing hash table for finding a post by unique datetime value

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size


    def _hash(self, key):
        return hash(key) % self.size


    def insert(self, key, value, name):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value, name)]
        else:
            for i, (k, v, n) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value, name)
                    break
            else:
                self.table[index].append((key, value, name))

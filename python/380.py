import random

class RandomizedSet:
    def __init__(self):
        self.vals = []
        self.val_to_index = {}

    def insert(self, val):
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val):
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last_val = self.vals[-1]
        self.vals[index] = last_val
        self.val_to_index[last_val] = index
        self.vals.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self):
        return random.choice(self.vals)

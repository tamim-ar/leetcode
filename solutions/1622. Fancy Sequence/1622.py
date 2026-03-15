MOD = 10**9 + 7

class Fancy:

    def __init__(self):
        self.seq = []
        self.mul = 1
        self.add = 0

    def modinv(self, x):
        return pow(x, MOD - 2, MOD)

    def append(self, val: int) -> None:
        val = (val - self.add) % MOD
        val = val * self.modinv(self.mul) % MOD
        self.seq.append(val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        self.mul = self.mul * m % MOD
        self.add = self.add * m % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % MOD
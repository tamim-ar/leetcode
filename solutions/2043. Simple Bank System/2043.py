class Bank:

    def __init__(self, balance: List[int]):
        self.bal = balance
        self.n = len(balance)

    def check(self, acc):
        return 1 <= acc <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.check(account1) or not self.check(account2):
            return False
        if self.bal[account1-1] < money:
            return False
        self.bal[account1-1] -= money
        self.bal[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.check(account):
            return False
        self.bal[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.check(account):
            return False
        if self.bal[account-1] < money:
            return False
        self.bal[account-1] -= money
        return True

class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento):
        self.balance = memento.balance

    def __str__(self):
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(100) # This is the initial state. State without Memento.
    m1 = ba.deposit(50) # First Memento.
    m2 = ba.deposit(25) # Second Memento.
    print(ba) # 175

    # restore to m1
    ba.restore(m1)
    print(ba) # 150

    # restore to m2
    ba.restore(m2)
    print(ba) # 175

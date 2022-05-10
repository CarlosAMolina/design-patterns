from abc import ABC
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, balance = {self.balance}")
            return True
        return False

    def __str__(self):
        return f"Balance = {self.balance}"


# Optional in Python as it uses Duck typing.
class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    def __init__(self, account, action, amount):
        self.amount = amount
        self.action = action
        self.account = account
        self.success = None  # Required to avoid invalid operations
        # that will cause incorrect results.
        # Like withdraw an amunt of money
        # that will incrase the balance.

    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        # Only undo if the operation was successful.
        if not self.success:
            return
        # strictly speaking this is not correct
        # (you don't undo a deposit by withdrawing)
        # but it works for this demo, so...
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == "__main__":
    ba = BankAccount()  # Balance = 0
    cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    cmd.invoke()
    print("After $100 deposit:", ba)  # Balance = 100

    cmd.undo()
    print("$100 deposit undone:", ba)  # Balance = 0

    # Example of invalid operation.
    # Without the `BankAccountCommand.sucess` attribute this would create
    # a positive balance.
    illegal_cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 1000)
    illegal_cmd.invoke()
    print("After impossible withdrawal:", ba)  # Balance = 0
    illegal_cmd.undo()
    print("After undo:", ba)  # Balance = 0

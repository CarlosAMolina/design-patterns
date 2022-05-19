# Composite Command a.k.a. Macro
# also: Composite design pattern ;)

import unittest
from abc import ABC, abstractmethod
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


class Command(ABC):
    def __init__(self):
        """Required to avoid erros like `test_transfer_fail`."""
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    def __init__(self, account, action, amount):
        super().__init__()
        self.amount = amount
        self.action = action
        self.account = account

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
        if not self.success:
            return
        # strictly speaking this is not correct
        # (you don't undo a deposit by withdrawing)
        # but it works for this demo, so...
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


# try using this before using MoneyTransferCommand!
class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=[]):
        super().__init__()
        for i in items:
            self.append(i)

    # Invoke the commands.
    def invoke(self):
        for x in self:
            x.invoke()

    # Important to undo in reverse order.
    def undo(self):
        for x in reversed(self):
            x.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    """Command to control incorrect transactions."""
    def __init__(self, from_acct, to_acct, amount):
        super().__init__(
            [
                BankAccountCommand(
                    from_acct, BankAccountCommand.Action.WITHDRAW, amount
                ),
                BankAccountCommand(to_acct, BankAccountCommand.Action.DEPOSIT, amount),
            ]
        )

    def invoke(self):
        """Required to sucess o fail all the chain."""
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        print("TEST 1")
        ba = BankAccount()
        deposit1 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
        deposit2 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 50)
        composite = CompositeBankAccountCommand([deposit1, deposit2])
        composite.invoke()
        print(ba) # Balance = 150
        composite.undo()
        print(ba) # Balance = 0

    def test_transfer_fail(self):
        """Here we don't check if it isn't enough money to 
        continue with the operations.
        """
        print("TEST 2")
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        # composite isn't so good because of failure
        amount = 1000  # try 1000: no transactions should happen
        wc = BankAccountCommand(ba1, BankAccountCommand.Action.WITHDRAW, amount)
        dc = BankAccountCommand(ba2, BankAccountCommand.Action.DEPOSIT, amount)

        transfer = CompositeBankAccountCommand([wc, dc])

        transfer.invoke()
        print("ba1:", ba1, "ba2:", ba2)  # ba1: Balance = 100 ba2: Balance = 1000 # end up in incorrect state
        transfer.undo()
        print("ba1:", ba1, "ba2:", ba2) # ba1: Balance = 100 ba2: Balance = 0


    def test_better_tranfer(self):
        print("TEST 3")
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 1000

        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print("ba1:", ba1, "ba2:", ba2) # ba1: Balance = 100 ba2: Balance = 0
        transfer.undo()
        print("ba1:", ba1, "ba2:", ba2) # ba1: Balance = 100 ba2: Balance = 0
        print("Success:", transfer.success) # Success: False


if __name__ == "__main__":
    unittest.main()

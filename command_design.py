from enum import Enum


class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):

        if command.action == Command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
            print(f"Successfully Deposited {command.amount}")

        elif command.action == Command.Action.WITHDRAW:
            if command.amount <= self.balance:
                self.balance -= command.amount
                command.success = True
                print(f"Successfully Withdrawn {command.amount}")
            else:
                command.success = False
                print(
                    f"Failed to Withdrawn from the account {command.amount\
                                                              }"
                )

    def __str__(self) -> str:
        return f"Balance {self.balance}"


if __name__ == "__main__":
    acc1 = Account()
    cmd = Command(Command.Action.DEPOSIT, 300)
    cmd1 = Command(Command.Action.WITHDRAW, 500)
    acc1.process(cmd)
    acc1.process(cmd1)

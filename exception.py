# Custom exception classes
class BankError(Exception):
    """Base class for all banking errors"""
    pass

class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance ₹{balance}, requested ₹{amount}")

class InvalidAmountError(BankError):
    pass

class DailyLimitExceededError(BankError):
    pass


class Account:
    DAILY_LIMIT = 20000

    def __init__(self, balance):
        self.balance = balance
        self.withdrawn_today = 0

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero")
        if self.withdrawn_today + amount > self.DAILY_LIMIT:
            raise DailyLimitExceededError("Daily withdrawal limit of ₹20000 exceeded")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)

        self.balance -= amount
        self.withdrawn_today += amount
        return self.balance


# Using it
account = Account(balance=5000)

for amount in [1000, -50, 9000, 30000]:
    try:
        new_balance = account.withdraw(amount)
        print(f"Withdrew ₹{amount}. Balance: ₹{new_balance}")
    except InsufficientFundsError as e:
        print(f"Error: {e}. Short by ₹{e.amount - e.balance}")
    except (InvalidAmountError, DailyLimitExceededError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Transaction attempt logged.\n")
from errors.insufficient_fund_error import InsufficientFundError

class BankAccount:
  def __init__(self, balance: float) -> None:
    if balance < 0:
      raise ValueError("balanace cannot be negative")
    self._balance = balance

  @property
  def balance(self) -> float:
    return self._balance

  def deposit(self, amount: float) -> None:
    if amount < 0:
      raise ValueError("The amount must be positive")

    self._balance += amount

  def withdraw(self, amount: float) -> None:
    if amount <= 0:
      raise ValueError("The withdrawal amount must be more than 0")

    if amount > self._balance:
      raise InsufficientFundError("Insufficient ammount for withdrawal")

    self._balance -= amount

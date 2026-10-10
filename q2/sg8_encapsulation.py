class BankAccount:

  def __init__(self, account_number: int, balance: float):
    self._account_number = account_number
    self._balance = 0.0
    self.balance = balance

  @property
  def account_number(self):
    return self._account_number

  @account_number.setter
  def account_number(self, value):
    self._account_number = value

  @property
  def balance(self):
    return self._balance

  @balance.setter
  def balance(self, value):
    if value >= 0:
      self._balance = value
    else:
      print("The balance must be not be a negative number.")


# --- Interactive Input ---
acc_num = int(input("Enter account number: "))
initial_balance = float(input("Enter initial balance: "))

a1 = BankAccount(acc_num, initial_balance)

print("\nOutput:")
print("Account 1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")

# Get new balance to update from user input
update_val = float(input("\nEnter balance to update: "))
print(f"Update balance to {update_val}")
a1.balance = update_val

print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")

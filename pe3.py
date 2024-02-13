import string
import datetime

def encode(input_text, shift):
  alphabet = list(string.ascii_lowercase)
  
  encoded_text = ""
  for char in input_text:
    if char.isalpha():
      index = alphabet.index(char.lower()) 
      new_index = (index + shift) % 26
      encoded_text += alphabet[new_index]
    else:
      encoded_text += char
  
  return (alphabet, encoded_text)

def decode(input_text, shift):

  alphabet = list(string.ascii_lowercase)  

  decoded_text = ""
  for char in input_text:
    if char.isalpha():
      index = alphabet.index(char.lower())
      new_index = (index - shift) % 26
      decoded_text += alphabet[new_index]
    else:
      decoded_text += char

  return decoded_text

class BankAccount:

  def __init__(self, name="Rainy", ID="1234", creation_date=datetime.date.today(), balance=0):
    self.name = name
    self.ID = ID
    if creation_date > datetime.date.today():
      raise Exception("Creation date cannot be in the future")
    self.creation_date = creation_date 
    self.balance = balance

  def deposit(self, amount):
    if amount < 0:
      print("Deposit amount cannot be negative")
      return
    self.balance += amount
    print(f"Deposit of {amount}. New balance is {self.balance}")

  def withdraw(self, amount): 
    self.balance -= amount
    print(f"Withdrawal of {amount}. New balance is {self.balance}")
  
  def view_balance(self):
    print(f"Current balance is {self.balance}")

class SavingsAccount(BankAccount):

  def withdraw(self, amount):
    
    if (datetime.date.today() - self.creation_date).days < 180:
      print("Withdrawals allowed only after 180 days")
      return

    if amount > self.balance:
      print("Overdraft not allowed")
      return
    
    self.balance -= amount
    print(f"Withdrawal of {amount}. New balance is {self.balance}")

class CheckingAccount(BankAccount):

  def withdraw(self, amount):
    
    if amount > self.balance:
      self.balance -= 30 # Charge overdraft fee
    
    self.balance -= amount
    print(f"Withdrawal of {amount}. New balance is {self.balance}")

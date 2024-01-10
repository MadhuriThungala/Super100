class BankAccount:
  def __init__(self,Account_holder_name,Account_number,Balance):
    self.Account_holder_name=Account_holder_name
    self.Account_number=Account_number
    self.Balance=Balance
  def deposit(self,amount):
    if(amount>0):
      self.Balance=Self.Balance+amount
  def withdraw(self,amount):
     if(amount>self.Balance):
        print("Balance is insufficient")
     else:
       self.Balance=Self.Balance-amount
       return self.Balance
  def display(self):
        print("Account holder Name:" ,self.Account_holder_name)
        print("Account number:",self.Account_number)
        print("Balance available:",self.Balance)


    

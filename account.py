
#
# Klasa przechowuje informacje o koncie bankowym
# oraz metody do zarządzania nimi
# deposit - wpłata środków na konto




# Inicjalizacja klasy BankAccount
class BankAccount:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    # withdraw - wypłata środków z konta
    def withdraw(self, amount):
        if amount > self.balance:
            print("Brak wystarczajacych środków")
        else:
            self.balance -= amount

    # checkBalance - sprawdzenie stanu konta
    def checkBalance(self):
        return self.balance
    
    # getAccountNumber - pobranie numeru konta
    def getAccountNumber(self):
        return self.accountNumber

class Transaction:
    def __init__(self, date, amount, description):
        self.date = date
        self.amount = amount
        self.description = description

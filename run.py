
from bank import Bank
from account import BankAccount
from person import Customer
from person import Employee
from client import CorporateClient



def run():
    
    bank = Bank("Sample Bank")
    account = BankAccount("1234567890", 1000)
    customer = Customer("Cd31", "Jack Daniels", "Burbon st", "785-644-3280")
    employee = Employee("En23", "Johnny Walker", "89 Blue St", "987-237-7863", "Boss")
    corporateClient = CorporateClient("GCLK", "Amco Inc.", "Amco Inc.", "985 Brooklyn")
    
 
    bank.createAccount(account)
    
    
    account.deposit(500)
    account.withdraw(200)
    
    
    print("Account balance:", account.checkBalance())
    

    print("Customer Name:", customer.getName())
    print("Customer Address:", customer.getAddress())
    print("Customer Phone:", customer.getPhoneNumber())
    
   
    print("Employee Name:", employee.getName())
    print("Employee Address:", employee.getAddress())
    print("Employee Phone:", employee.getPhoneNumber())
    print("Employee Designation:", employee.getDesignation())
    
   
    print("Client ID:", corporateClient.getClientID())
    print("Client Type:", corporateClient.getClientType())
    print("Client Name:", corporateClient.getClientName())
    print("Business Name:", corporateClient.getBusinessName())
    print("Business Address:", corporateClient.getBusinessAddress())

if __name__ == "__main__":
    run()

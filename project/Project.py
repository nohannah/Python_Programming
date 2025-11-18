import os
Data_file="account.txt"
def load_accounts():
    accounts= {}
    if os.path.exists(Data_file):
        with open(Data_file, 'r') as file:
            for line in file: 
                account_id ,name, balance=line.strip().splip(',')
                accounts[account_id] ={"name" : name , "balance": float(balance)}
                return accounts
def save_accounts(accounts):
    with open(Data_file, "w") as file : 
     for account_id, name , balance in accounts.items(): 
         file.write(f"{account_id},{name},{balance}\n")

def create_account(accounts):
    account_id = input("Enter account ID: ")
    if account_id  in accounts: 
        print("Account already exists.")
        return
    name = input("Enter account holder name:")
    balance= float(input("Enter the balance: "))
    
    accounts[account_id] = { "name" : name , "balance" : balance}
    print("Account create successfully.")      
def deposit(accounts):
    account_id= input("Enter account ID:")
    if account_id not in accounts: 
        print("Account is not found.")
        return 
    balance = float(input("Enter deposit amount:"))  
    accounts[account_id]["balance"] += balance
    print("Deposit successfull.")   
def withdraw(accounts):
    account_id= input("Enter account ID:")
    if account_id not in accounts: 
        print("Account is not found.")
        return 